def gcd(a, b):
    if a == b: return a
    while b > 0: a, b = b, a % b
    return a


def solve():
    fact=[10,7,9,43,16,8]
    print(1,2)
    ab=int(input())
    print(1,3)
    ac=int(input())
    print(4,5)
    de=int(input())
    print(4,6)
    df=int(input())
    for i in fact:
        if ab % i == 0 and ac % i == 0:
            a = i
            break
    b = ab // a
    c = ac // a
    if b == 5:
        b = 10
        a //= 2
        c *= 2
    if c == 5:
        c = 10
        a //= 2
        b *= 2

    for i in fact:
        if de % i == 0 and df % i == 0:
            d = i
            break
    e = de // d
    f = df // d

    if e == 5:
        e = 10
        d //= 2
        f *= 2
    if f == 5:
        f = 10
        d //= 2
        e *= 2

    print(a,b,c,d,e,f,"is the exact order of 6 numbers")


















solve()


