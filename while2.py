#While_2

#input 

print("╔═══════════════════════════╗")
H = int(input("Digite su Numero: "))
print("╚═══════════════════════════╝")

#proccesing

Q = H/5
N = 0

while H>=Q:
    H = H - 0.1 * H
    N = N + 1


# Output

print("╔═════════════════════════════════════════════════════════════════╗")
print("Los rebotes desde el valor digitado en total son: "+str(N))
print("╚═════════════════════════════════════════════════════════════════╝")