#import math


def check(my_list, start, end):
    perfect_square = []
    for num in range(start, end+1):
        if int(my_list[num] ** 0.5) == (my_list[num] ** 0.5):
            #print(my_list[num])
            perfect_square.append(my_list[num])
    print("The perfect square numbers in your list are : ", perfect_square)


my_list = []
n = int(input("Enter number of elements : "))
print("Enter your elements : ")
for i in range(n):
    element = int(input())
    my_list.append(element)
x, y = input("Enter 2 indices to check between them : ").split()

check(my_list, int(x), int(y))
