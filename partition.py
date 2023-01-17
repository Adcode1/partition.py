def swap(i,j,lst):
    temp=lst[i]
    lst[i]=lst[j]
    lst[j]=temp
def partition(lst,x):
    i=0
    j=(len(lst)-1)
    while i<j and lst[i]<x:
        i=i+1
    while i<j and lst[j]>=x:
        j=j-1
    while i<j:
        swap(i,j,lst)
        while i<j and lst[i]<x:
            i=i+1
        while i<j and lst[j]>=x:
            continue
    (p1,p2)=(lst[0:j],lst[j:len(lst)])
