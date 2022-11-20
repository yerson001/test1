import time

def suma(num):
    if num == 1:
        return 1
    else:
        return num + suma(num-1)

def sumlist(lista,index):
    if index == len(lista):
        return 0
    return lista[index] + sumlist(lista,index+1)




print(sumlist([4,1,2,5,3],0))
time.sleep(1)
