"""
1、python 的输入是字符串,需要自己转型
2、strip去掉左右两端的空白符,返回str, lstrip去掉左边的空白字符
3、slipt将字符串按空白符拆开,返回[str]
4、map 将list里面的值映射到指定类型,返回[type]
5、EOF用来抓异常
6、print(val, end = " ")就不会换行,否则反之
"""

class Test:
    def func1(self):
        """对10个正整数进行大小比较
        测试数据：9 8 6 3 9 13 5 7 18 31
        """
        a_1 = input() #读取一行
        # b_1是一个列表,将a_1读取的10个字符串类型的整数按空格分割，并对每个数强制转型为int类型
        b_1 = [int(n) for n in a_1.split(' ')]
        b_1.sort()
        for i in b_1:
            print(i,end = " ") # 输出, 
        print()
    
    # 没有告诉几组数据，但每组数据有两个数，输出两个数的和
    def func2(self):
        while True:
            try:
                a,b = map(int,input().strip().split())
                print(a+b)
            except EOFError:
                break

    # 第一个数是整数，告诉是几组数据，剩下的行是每组的数据
    def func3(self):
        tcase = int(input().strip()) # 一个数据去除空白字符后，直接用int()转型
        for case in range(tcase):
            a,b = map(int,input().strip().split()) # 每组数据包括a,b两个
            print(a+b)

    # 第一行的整数表示一共几组数据，剩下的行每一行第一个数字代表这一组共有几个数据。
    def func4(self):
        tcase = int(input().strip())
        for case in range(tcase):
            data = list(map(int,input().strip().split()))
            n,array = data[0],data[1:]
            print(sum(array))

    # 输入有两行，第一行n 。第二行是n个空格隔开的字符串
    def func5(self):
        n = int(input())
        words = [x for x in input().strip().split()]
        words.sort()

        for word in words:
            print(word,end=" ")
        print()
    

    def func5(self):
        list = [] #定义
        list.append(a) #在数组的末尾添加元素a
        list.insert(i,a) #i为在哪一个位置插入a
        list.extend([]) # 把某个列表插到list中，参数是一个列表
        list.index(a) #在列表中搜索元素a，返回其位置
        list.index(a,0,5) #在0,5搜索
        list.remove(a) #删除第一个次出现的a
        len(list) #列表长度
        del list #把list在内存中清除
        del list[1] #把list[1]删除
        list[1:3] #只是拷贝 list[1],list[2] （3-1=2只有两个元素）
        list1 = list[:] #列表拷贝
        list2 = list #只是相等，list变，list2也变，只是指定另一个名字罢了
        #列表之间的比较 默认从[0]开始
        list = list1 + list2 # 合并列表
        list * 3
        # 列表判断元素
        a in list 
        a not in list
        list.count(a) #a在list中出现的次数
        list.reserve() #翻转
        list.sort() #升序
        list.sort(reserve = true) #从大到小,降序

if __name__ == "__main__":
    test = Test()
    # test.func5()
    test.func4()
