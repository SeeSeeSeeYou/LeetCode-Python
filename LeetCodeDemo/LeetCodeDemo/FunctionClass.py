class FunctionClass(object):
    """this is a function class""" 

from collections import Counter
import sys
import re  

#将两个列表合并，去除重复元素后升序输出
def sortArrayWithSet(self,arr1:[int],arr2:[int]): 
    arr =[]
    for a1 in arr1:
        arr.append(a1)
    for a2 in arr2:
        arr.append(a2) 
    arr=list(set(arr)); 
    for a in arr:
        print(a)

#定义一个多层嵌套的列表[1,2,3,[5,2,4,6,[9,5,8,6,7]]]
def printArr(self,arr:[int])->[int]:
    result=[]
    for a in arr:
        if isinstance(a,list): 
            printArr(a)
        else:
            print(a)
            result.append(a)     
    return result


#猜数字
#输入: secret = "1807", guess = "7810"
#输出: "1A3B"
#解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。
def getHint(self, secret: str, guess: str) -> str:  
    s_c=Counter(secret)
    g_c=Counter(guess)
    a=0
    b=0
    for x,y in zip(secret,guess):
        if x==y:
            s_c[x]-=1
            g_c[y]-=1
            a+=1
    for i in s_c & g_c:
            b+=min(s_c[i],g_c[i])
    return "{}A{}B".format(a,b)


#给定一个无序的整数数组，找到其中最长上升子序列的长度。
#输入: [10,9,2,5,3,7,101,18]
#输出: 4 
#解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。 
def lengthOfLIS(self, nums: List[int]) -> int:
    if not nums: return 0
    length =len(nums)
    resultArr=length * [1]
    for i in range(length):
        for j in range(i):
            if nums[j]<nums[i]:
                resultArr[i]=max(resultArr[i],resultArr[j]+1)
    return len(resultArr)