x = 11
y = 19

Ha = x+y
print("Ha = ", Ha)

Hb = Ha+10.5
print("Hb = ", Hb)

Hc = int(Hb)
print("Hc = ", Hc)

Hd = Ha/Hb
print("Hd = ", Hd)

isinstance(Hd, int)

isinstance(Hd, float)

if isinstance(Hd, int):
    print("Hd adalah bilangan integer!")
else:
    print("Hd adalah bilangan float!")

isinstance(object, type)