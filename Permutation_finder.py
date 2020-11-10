#Generates permutations for numbers greater than 3
ans=[]
def swap(ls,ele):
    sa=ls.copy()
    i=0
    j=0
    while i<len(ls):
        while j<len(ls):
            if i!=j:
                ls[i],ls[j]=ls[j],ls[i]
                new=ele+ls.copy()
                if new not in ans:
                    ans.append(ele+ls.copy())
                ls=sa.copy()
                j+=1
            else:
                j+=1
        i+=1
        j=0

def rotate(l,i):
    temp=l[i:].copy()
    rem=l[:i].copy()
    return temp+rem

l=list(map(int,input().split()))
l1=l.copy()
r=1
while r<=len(l):
    ele=l1[:1]
    s=l1[1:].copy()
    swap(s,ele)
    l1=rotate(l,r)
    r+=1

o=1
w=len(l)
s=1
while w>1:
    s*=w
    w-=1
f=[]
#Change the limit to 100 to greater value for getting permutations of greater number
while o<=100:
    if len(f)==s:
        break
    for i in ans:
        if i not in f:
            f.append(i)
    ans1=ans.copy()
    ans.clear()
    for i in ans1:
        l2=i.copy()
        q=2
        while q<=len(l2):
            ele1=l2[:q]
            t=1
            s1=l2[q:].copy()
            while t<len(s1):
                swap(s1,ele1)
                l2=rotate(l2,t)
                t+=1
            q+=1
    o+=1
for i in f:
    print(i)
print("Length of total permutations:",len(f))
