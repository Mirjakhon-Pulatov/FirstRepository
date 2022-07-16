#country = ['USA','UK','UZB','RUS','Kaz','Tadj','Krgyz','Trkm']
#country.reverse()
#print(country).
#print(sorted(country, reverse=True))
#son = list(range(120,1201,2))
#taomlar = ['osh','manti','somsa','chuchvara','kabob']
#nonushta1 = ['manti', 'somsa', 'chuchvara', 'kabob', 'six-kabob', 'six-somsa','six']
#nonushta1 = tuple(nonushta1)
#ismlar = ['Ali','Vali','Hasan','Husan','Miron']
#for i in ismlar:
#    print("Salom", i)
#print("Kod",len(ismlar),"marta takrorlandi")
#tsonlar = list(range(11,100,2))
#b=[]
#for i in tsonlar:
#    b.append(i**3)
#print(b)
#tanishlar = []
#print("Bugun suhbatlashgan odamlaringizdan 5 tasini kiriting: ")
#for i in range(5):
 #   tanishlar.append(input(f"{i+1} - suhbatlashgan odamingizni kiriting: "))
#print(tanishlar)

#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for i in cars:
#    if i != 'gm':
#        print(i.title())        
#    else:
#        print(i.upper())

#print("ismingizni kiriting: ")
#login = input(">>> ")
#if login.lower() == 'admin':
#    print("Salom Admin. Foydalanuvchilar ro\'yxatini ko\'rishni xohlaysizmi")
#else:
#    print(f"Salom {login}")

#print("2 ta son kiriting: ")
#a,b = list(map(int,input().split()))
#if a == b:
#    print('Sonlar teng ekan')
#else:
#    print('xato')

    
#print("Juft son kiriting: ")
#a = int(input(">>> "))
#if a % 2 == 0:
#    print("Rahmat")
#elif a % 2 == 1:
#    print("Bu juft son emas")

yosh = int(input("Yoshingiz nechida?"))
if yosh<=4 or yosh>=60:
    narh = 0;
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")


