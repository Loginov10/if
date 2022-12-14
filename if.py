from math import *
from random import *
print("Sisselogimine tahvel")
try:
    vanus=int(input("kui vana sa oled ?"))
    if vanus>=18:
        print("Kas sa annad vanematele loa oma Tahvelit vaadata ?")
        a=(input("Jah või ei"))
        if a.lower()=="jah":         #lower делает все буквы маленькими
            print({a})
            print("See on ligipääs teie vanematele")
            print("tahvel on linni")
        elif a.upper()=="ei":           #upper делает все буквы большими
            print("Sissepääs pudub")
            print("Tahvel on kinni")
    if vanus<18:
        print("Juurepääs vanematele on automaatselt antud")
except:
    print("Tahvel on kinni")







try:
   päev=int(input("Mis päev ja mitu tundi täna on"))
   if päev==1:
        n="Esmaspäev"
        n="6 tundi"
   elif päev==2:
        n="Teisipäev"
        n="8 tundi"
   elif päev==3:
        n="Kolmapäev"
        n="6 tundi"
   elif päev==4:
        n="Neljapäev"
        n="5 tundi"
   elif päev==5:
        n="Reede"
        n="7 tundi"
   elif päev==6:
        n="Laupäev"
        n="0 tundi"
   elif päev==7:
        n="Pühapäev"
        n="0 tundi"

except:
    print("!!!!!")











#13/12/22
try:
    aa=int(input("на сколько лет делаете взнос в банк ?"))
    bb=randint(0,1000000)
    print(f"взнос составляет {bb} ")
    cc=float(input("какой поцент (%) годовых ?"))
    
    if bb>1000001:
        print("слишком большой взнос")
    elif cc>101:
        print("слишком большой процент")
    elif bb<0:
        print("таких денег нет")
    elif cc<0:
        print("ух че захотел")
    else:
        print(f"")
except:
    print("!!!!!")




a=randint(0,100)
b=randint(0,100)
print(f"a={a}\b={b}")
if a>b:
    print("a={a} on suurem kui b={b}")
elif b>a:
    print("b={b} on suurem kui a={a}")
else:("!!!!")



r=randint(0,100)
a=randint(0,100)
print(f"r={r}\na={a}")
if r>0 and a>0:
    Skv=a**2
    Skr=pi*r**2
    if Skv>Skr:
        print(f"Ruudu pindala {Skv} on suurem ringi pindala {Skr}")
    elif Skr>Skv:
          print("Ringi pindala {Skv} on suurem ruudu pindala {Skv}")
    else:
        print("Pindalad on võrdsed. {Skr}")
else:
    print(f"{a} ja {r} peavad > kui 0 olla")
