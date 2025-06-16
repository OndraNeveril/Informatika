from random import randint
file = open("save.txt")
p = int(file.readline())
pp = int(input(f"Kolik chceš vsadit? Minimální sázka je 10, máš celkem {p}. "))
if pp > p or pp <10:
    exit()
fileout = open("save.txt", "w")

def prohra(p, m):
    p -= m
    fileout.write(str(p))

def výhra(p, m):
    p += m
    fileout.write(str(p))

k = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]


s = 0
ss = k.pop(randint(0, len(k) - 1))
if ss >= 10:
    ss = 10
if s <= 10 and ss == 1:
    ss = 11
s += ss

d = 0
dd = k.pop(randint(0, len(k) - 1))
if dd >= 10:
    dd = 10
if d <= 10 and dd == 1:
    dd = 11
d += dd

print(f"Dealer má {d} a jednu další kartu")

dd = k.pop(randint(0, len(k) - 1))
if dd >= 10:
    dd = 10
if d <= 10 and dd == 1:
    dd = 11
d += dd

while True:
    ss = k.pop(randint(0, len(k) - 1))
    if ss >= 10:
        ss = 10
    if s <= 10 and ss == 1:
        ss = 11
    s += ss
    if s > 21:
        print(f"Máš {s}, prohrál jsi!")
        prohra(p, pp)
        exit()
    else:
        if input(f"Máš {s}, chceš další kartu? ANO/NE ") == "NE":
            break

while d < 17:
    print(f"Dealer  má  {d}")
    dd = k.pop(randint(0, len(k) - 1))
    if dd >= 10:
        dd = 10
    if d <= 10 and dd == 1:
        dd = 11
    d += dd
    if d > 21:
        print(f"Dealer má {d}, prohrál")
        výhra(p, pp)
        exit()
print(f"Dealer má {d}")
if d > s:
    print("Dealer má více a proto vyhrál")
    prohra(p, pp)
elif s > d:
    print("Máš více, než dealer, vyhrál jsi!")
    výhra(p, pp)
else:
    print("Máte oba stejně, remíza")
    fileout.write(str(p))