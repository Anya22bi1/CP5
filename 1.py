def CC(x, y):
    if y == 2:
        cc = bin(x)[2:]    #Перевод в 2ую сс
    else:
        cc = oct(x)[2:]    #Перевод в 8ую сс
    return cc

A = int(input("Введите целое число: "))
sist = int(input("Введите систему счисление 2 или 8: "))
pr_cc = CC(A, sist)
print("Число в системе счисления", sist, ":", pr_cc)
