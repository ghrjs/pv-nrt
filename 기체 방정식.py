
R=float(input("기체 상수를 입력하세요."))

a=input("구하려는 변수를 입력하세요.(P, V, n, T)")


if a == "P":
    b=float(input("부피(L)를 입력하세요."))
    c=float(input("몰수(몰)를 입력하세요."))
    d=float(input("절대 온도(K)를 입력하세요."))
    i=R*c*d
    i=i/b
    print("기체의 압력은",i,"atm입니다!")

elif a == "V":
    b=float(input("압력을 입력하세요."))
    c=float(input("몰수(몰)를 입력하세요."))
    d=float(input("절대 온도(K)를 입력하세요."))
    i=R*c*d
    i=i/b
    print("기체의 부피는",i,"L입니다!")

elif a == "n":
    b=float(input("부피(L)를 입력하세요."))
    c=float(input("압력을 입력하세요."))
    d=float(input("절대 온도(K)를 입력하세요."))
    i=b*c
    i=i/R
    i=i/d
    print("기체의 몰수는",i,"몰 입니다!")

elif a == "T":
    b=float(input("부피(L)를 입력하세요."))
    c=float(input("몰수(몰)를 입력하세요."))
    d=float(input("압력을 입력하세요."))
    i=b*d
    i=i/R
    i=i/c
    print("기체의 절대온도는",i,"K입니다!")

else:
    print("잘못 입력하셨습니다.")