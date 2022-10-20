num=float(input("Введите число: "))
a=int(input("Введите целевую систему счисления: "))
while a != 2 and a != 8:
    print("Выберете двоичную или восьмеричную систему счисления!")
    a=int(input("Введите целевую систему счисления: "))

def number(i,k):
    p=int(i)
    t=i-p
    vi=i
    vk=k
    block=0
    v = ''
    vt = ''
    vp = ''
    while p > 0 :
        vp = str(p % k) + vp
        p //= k
    if t != 0:
        while int(t) == 0  and block < 50:
            vt = vt + str(int((t-int(t)) * k)) 
            t = (t-int(t)) * k
            block = block + 1
        while int(t) > 0 and block < 50 :
            vt = vt + str(int((t-int(t)) * k)) 
            t = (t-int(t)) * k
            block = block + 1
        v = vp + "." + vt
    else:
        v=vp
    print ("Вывод: ",vi ,"->", v)

number(num,a)
