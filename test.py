# -*- coding: utf-8 -*-
"""
用来测试各种函数及想法
"""
import requests as req
import re
import io
import argparse
# link = 'http://python.usyiyi.cn/python_278/library/argparse.html'
#
# strs = "git使用之二——.gitignore文件详解 - 简书"
# t = io.BytesIO()
# t.write(strs.encode('utf-8'))
# print(t.getvalue())
# f = open('.\down_text\git使用之二——.gitignore文件详解 - 简书.txt', 'rb')
# print(f.read())
# f.close()
# class FooAction(argparse.Action):
#     def __init__(self,option_strings, dest, nargs=None, **kwargs):
#         if nargs is not None:
#             raise ValueError("nargs not allowed")
#         super(FooAction, self).__init__(option_strings, dest, **kwargs)
#
#     def __call__(self, parser, namespace, values, option_string=None):
#         # print('%r %r %r' % (namespace, values, option_string))
#         global link
#         link = values
#         setattr(namespace, self.dest, values)
#
#
# parser = argparse.ArgumentParser(description='学习这个模块怎么用', prog='PROG')
# # ?.*+ 符合正则表达式的语法
# parser.add_argument('baz', nargs='*', help='收集不带参数的*个值')
# parser.add_argument('-sc', action='store_const', const=10, help='有参数时为指定的 const值（任意值）')
# parser.add_argument('-f', action='store_true', help='有参数为 action指定的 true或false')
# parser.add_argument('-foo', action='append', help='将多个参数追加到列表')
# parser.add_argument('--s', dest='types', action='append_const', const=str, help='有参数时追加类型str到列表')
# parser.add_argument('-c', action='count', help='记录参数出现的次数')
# parser.add_argument('--version', action='version',
#                     version='%(prog)s 2.0', help='输出版本号 (prog)表示文件名或ArgumentParser中定义的prog值')
# parser.add_argument('-debug', nargs=1, help='参数-bar需要nargs指定数量的值')
# parser.add_argument('-bar', nargs='?', const='abc', default='True', help='参数-bar接受0个或一个参数 可配合const或其他参数使用')
# parser.add_argument('args', nargs=argparse.REMAINDER, help='收集其余所有参数到一个列表，就是收集无效多余的参数 ')
# parser.add_argument('-move', choices=['rock', 'paper', 'scissors'], help='限定参数的范围')
# parser.add_argument('-door', type=int, choices=range(1, 4), help='限定参数范围')
# parser.add_argument('--required', required=False, help='设定为必选参数')
# parser.add_argument('-a', metavar='0-9', type=int, default=0, choices=range(10), help='metavar 生成帮助信息，它需要一些方式来指代期望的参数。')
# parser.add_argument('--xoo', dest='bar',help='允许提供自定义属性名称 %(dest)s')
#
# parser.add_argument('--soo', action=FooAction)
# parser.add_argument('x')
# parser.add_argument('-r', nargs=1, type=int, choices=range(0, 8), help='最大请求失败重试次数')
#
# args = parser.parse_args('1 -r 1'.split())
# print(args)
# print(link)


class chinese_to_digits(object):
    def __init__(self):
        self.common_used_numerals = {u'零': 0, u'一': 1, u'二': 2, u'三': 3, u'四': 4, u'五': 5, u'六': 6, u'七': 7, u'八': 8,
                                u'九': 9, u'十': 10, u'百': 100,
                                u'千': 1000, u'万': 10000, u'亿': 100000000}

    def run(self, uchars_cn):
        s=uchars_cn
        if not s :
            return 0
        for i in [u'亿',u'万',u'千',u'百',u'十']:
            if i in s:
                ps=s.split(i)
                lp=self.run(ps[0])
                if lp==0:
                    lp=1
                rp=self.run(ps[1])
                # print(i,s,lp,rp,'\n')
                return lp*self.common_used_numerals.get(i, 0)+rp
        return self.common_used_numerals.get(s[-1], 0)

# c2d = chinese_to_digits()
# print(c2d.run('第三十三章'))

###
def reserved_format(self):
    import keyword
    import builtins
    k = dict(zip(keyword.kwlist, list(map(lambda x: '{} '.format(x), keyword.kwlist))))
    b = dict(zip(dir(builtins),  list(map(lambda x: '{} '.format(x), dir(builtins)))))
    leave_dict = dict(k, **b)
    def re_sub(t):
        self.body = re.sub(pattern='^{}'.format(t[0]), repl=t[1], string=self.body, flags=re.M)
    list(map(re_sub, leave_dict.items()))


# ----------------------------------------

# DBUG   = 0
#
# reBODY =re.compile( r'<body.*?>([\s\S]*?)<\/body>', re.I)
# reCOMM = r'<!--.*?-->'
# reTRIM = r'<{0}.*?>([\s\S]*?)<\/{0}>'
# reTAG  = r'<[\s\S]*?>|[ \t\r\f\v]'
# reOTH  = r'(&nbsp;)*'
# reIMG  = re.compile(r'<img[\s\S]*?src=[\'|"]([\s\S]*?)[\'|"][\s\S]*?>')
#
# class Extractor():
#     def __init__(self, url = "", blockSize=3, timeout=5, image=False):
#         self.url       = url
#         self.blockSize = blockSize
#         self.timeout   = timeout
#         self.saveImage = image
#         self.rawPage   = ""
#         self.ctexts    = []
#         self.cblocks   = []
#
#     def getRawPage(self):
#         try:
#             resp = req.get(self.url, timeout=self.timeout)
#         except Exception as e:
#             raise e
#
#         if DBUG: print(resp.encoding)
#
#         resp.encoding = "gbk"
#
#         return resp.status_code, resp.text
#
#     def processTags(self):
#         self.body = re.sub(reCOMM, "", self.body)
#         self.body = re.sub(reTRIM.format("script"), "" ,re.sub(reTRIM.format("style"), "", self.body))
#         # self.body = re.sub(r"[\n]+","\n", re.sub(reTAG, "", self.body))
#         self.body = re.sub(reTAG, "", self.body)
#         self.body = re.sub(reOTH, '', self.body)
#
#     def processBlocks(self):
#         self.ctexts   = self.body.split("\n")
#         self.textLens = [len(text) for text in self.ctexts]
#
#         self.cblocks  = [0]*(len(self.ctexts) - self.blockSize - 1)
#         lines = len(self.ctexts)
#         for i in range(self.blockSize):
#             self.cblocks = list(map(lambda x,y: x+y, self.textLens[i : lines-1-self.blockSize+i], self.cblocks))
#
#         maxTextLen = max(self.cblocks)
#
#         if DBUG: print(maxTextLen)
#
#         self.start = self.end = self.cblocks.index(maxTextLen)
#         while self.start > 0 and self.cblocks[self.start] > min(self.textLens):
#             self.start -= 1
#         while self.end < lines - self.blockSize and self.cblocks[self.end] > min(self.textLens):
#             self.end += 1
#
#         return "\n".join(self.ctexts[self.start:self.end]).strip()
#
#     def processImages(self):
#         self.body = reIMG.sub(r'{{\1}}', self.body)
#
#     def processText(self):
#         '''删除特定组合的内容'''
#         lists = ("（快捷键←）上一章|返回目录|加入书签|推荐本书|返回书页|下一章（快捷键→）",
#                  "投推荐票回目录标记书签"
#                  )
#         for n in lists:
#             try:
#                 self.text = self.text[:self.text.index(n)]
#             except BaseException:
#                 continue
#             else:
#                 break
#
#
#     def getContext(self):
#         code, self.rawPage = self.getRawPage()
#         try:
#             self.body = re.findall(reBODY, self.rawPage)[0]
#         except BaseException:
#             self.body = self.rawPage
#         if DBUG: print(code, self.rawPage)
#
#         if self.saveImage:
#             self.processImages()
#         self.processTags()
#         self.text = self.processBlocks()
#         self.processText()
#         return self.text
        # print(len(self.body.strip("\n")))


# if __name__ == '__main__':
#     ext = Extractor(url="http://www.52dsm.com/chapter/6712/3284687.html", blockSize=5, image=False)
#     print(ext.getContext())

# ----------------------------------------
#
def img(x=[]):
    len_x = len(x)  # x轴长度
    len_y = max(x)  # y轴长度

    x_y = []
    for a in x:
        none_y = [False] * len_y  # 空白y轴
        temp = none_y
        for b in range(a):
            temp[b] = True
        x_y.append(temp)

    y_x = []
    for c in range(len_y):
        temp2 = []
        temp2.append('{:<{}} |'.format(str(len_y - c), len(str(len_y))))
        for d in x_y:
            s = d[len_y - c - 1]
            if s:
                temp2.append('x' * 10)
            else:
                temp2.append(' ' * 10)
        y_x.append(''.join(temp2))
    for x in y_x:
        print(x)

import matplotlib.pyplot as pyplot


k = 5
c_texts = '<span \nclass="n">\n&lt;module&gt\n;</span><span class="st\n">感覺閾\n' \
          '限（英语：Sensory threshold）是\n' \
          '学术\n' \
          '\n' \
          '研究中的\n' \
          '常用语，指令对象发生某种变化<\ndiv class="sign" \n' \
          'style="\nmax-height:500px;maxH\neightIE:500px;">不知道睡了多久的席梦实醒来，\n发现黄永\n' \
          '胜就\n' \
          '坐在自己床边，在黄永胜旁边的居然是林彪\n，黄永胜指着其余三个人介绍道：这位是115师的李作' \
          '鹏参谋，另外两位挂着新四军胸章的，一位叫邱会作，新四军四师所需的某种条件的值。阈值根据条' \
          '件本身可以有不同的单位。阈值被广泛运用在&nbsp;...</span\n><font color="#999999">我之前就提' \
          '议先把北方难民组织成民团进驻有烽火台和信号弹的堡垒式农庄压到广东来卡点，' \
          '<font size="4">下半晌开始，李庄集中热闹了起来，打谷场的戏台上，戏子们脸涂白粉，咿咿呀呀的唱着粤北采茶' \
          '戏。游走各乡的小贩们挑着扁担，一头挂一支灯笼，一头插一个拨浪鼓，一边随着拨浪鼓的声音穿梭在人群之中，一边' \
          '吆喝着自己的买卖。有走累的，便在附近树下，借助火把的光线把摊位支了起来，摇着鼓招呼着游人。一时间，小小' \
          '的李庄集也不输于逍遥圩的繁.n\n</font>华热闹。\n</font>\n\n这些'
c_texts = c_texts.split('\n')
lines = len(c_texts)
c_block = []
c_texts_lens = [len(x) for x in c_texts]        # 每行的长度
for x in range(len(c_texts) - k + 1):
    c_block.append(sum([len(y) for y in c_texts[x:x+k]]))

max_block = max(c_block)                    # 最大的块
start = end = c_block.index(max_block)      # 定位最大的块

while start >= 0 and c_block[start] > min(c_block):
    start -= 1
while end < len(c_block) - 1 and c_block[end] > min(c_block):
    end += 1

re_text = '\n'.join(c_texts[start + k: end + k - 1])
# ----------------------------------------

# pyplot.plot(c_block)
# pyplot.ylabel('test')
# pyplot.show()

import multiprocessing

def read(que):
    mu_list = {}
    n = 0
    while True:
        value = que.get(block=True)
        if value == None:
            break
        print(value)
        mu_list[str(n)] = multiprocessing.Process(target=draw, args=(value,))
        mu_list[str(n)].daemon = False
        start = mu_list[str(n)]
        start.start()
        n += 1

def draw(c_blocks):
    pyplot.plot(c_blocks)
    pyplot.ylabel('c_block data')
    pyplot.show()

# if __name__=='__main__':
#     q = multiprocessing.Queue()
#     # q = queue.Queue()
#     mu = multiprocessing.Process(target=read, args=(q,))
#     mu.start()
#
#     a = [2,3,4,5,7,8,55,3,4,5,66,4,4]
#     b = [22,33,4,25,17,8,55,3,4,5,66,14,4]
#     q.put(a)
#     q.put(b)
#     q.put(None)

import requests
from bs4 import BeautifulSoup

nort = 'http://bbs.northernbbs.com/thread-671618-1-1.html'
tieba = 'http://tieba.baidu.com/p/4838122410?pn=5'
pconline = 'http://pad.pconline.com.cn/846/8465468_1.html'
piaotian = 'http://www.piaotian.net/html/5/5924/3200728.html'
hacg = 'https://www.hacg.li/wp/'

headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                   ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
               }

r = requests.get('http://chuangshi.qq.com/bk/ls/AGoENV1mVjQAP1Rk-r-550.html', headers=headers)



htmlbs = BeautifulSoup(r.content, 'html5lib')
p = htmlbs.find(id='chaptercontainer')
p2 = p.contents

up = htmlbs.find('a', string=re.compile(r'上一|[nN][eE]?[xX][tT]|&lt'))
up2 = htmlbs.find('a', class_=re.compile(r'[pP][rR]?[eE][vV]'))


down = htmlbs.find('a', string = re.compile('下一|[nN][eE]?[xX][tT]|&gt;'))
down2 = htmlbs.find('a', class_= re.compile(r'[nN][eE]?[xX][tT]'))
pass


def merge(switch=False):
    def merge_func(func):
        def wrapper(*args, **kwargs):
            if switch:
                pass
            return func(*args, **kwargs)
        return wrapper
    return merge_func