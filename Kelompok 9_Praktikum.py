from pylab import * 

def f(x):
    return x ** 3 - 3* x + 1

x = linspace(-1000, 1000, 10)

x1 = float(input("Masukkan X1 : "))
x2 = float(input("Masukkan X2 : "))

x3 = (x1 + x2) / 2

counter = 1
while abs(f(x3)) > 0.001:
    print("Iterasi ke - ", counter)
    print("X1 = ", x1)
    print("X2 = ", x2)
    print("X3 = ", x3)
    print (" ")
    if f(x1) * f(x3) > 0:
        x1 = x3
    else: 
        x2 = x3
    x3 = (x1 + x2) / 2
    counter += 1

print("Hasil akhir = ", x3)

plot(x,f(x))

xlabel('sb x')

ylabel('sb y')

title('Metode Bolzano')

grid(True)

show()