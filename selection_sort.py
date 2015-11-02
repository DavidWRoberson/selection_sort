import random

numbers = []
x = 1
while(x < 101):
	y = (random.random()) * 10000
	numbers.append(y)
	x += 1




def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

selectionSort(numbers)
print(numbers)