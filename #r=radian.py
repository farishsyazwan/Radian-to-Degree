def radiantodegree():
    #r=radian
    #p=perpuluhan
    import math
    r=int(input("Insert radian: "))
    p=int(input("How many decimal point?(0-14)"))
    #d=degree
    PI=math.pi
    d=r*(180/PI)
    if p == 0:
        d=round(d)
        print(d)
    elif p == 1:
        d=format(d,".1f")
        print(d)
    elif p == 2:
        d=format(d,".2f")
        print(d)
    elif p == 3:
        d=format(d,".3f")
        print(d)
    elif p == 4:
        d=format(d,".4f")
        print(d)
    elif p == 5:
        d=format(d,".5f")
        print(d)
    elif p == 6:
        d=format(d,".6f")
        print(d)
    elif p == 7:
        d=format(d,".7f")
        print(d)
    elif p == 8:
        d=format(d,".8f")
        print(d)
    elif p == 9:
        d=format(d,".9f")
        print(d)
    elif p == 10:
        d=format(d,".10f")
        print(d)
    elif p == 11:
        d=format(d,".11f")
        print(d)
    elif p == 12:
        d=format(d,".12f")
        print(d)
    elif p == 13:
        d=format(d,".13f")
        print(d)
    elif p == 14:
        print(d)
    else:
        print("Nilai yang dimasukkan tidak diterima")
radiantodegree()