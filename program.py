def f(x):
    return x**3 - 4*x - 9

def df(x):
    return 3*x**2 - 4

x = 2.5

for i in range(10):
    x_baru = x - f(x)/df(x)

    if abs(x_baru - x) < 0.00001:
        break

    x = x_baru

print("Akar =", x_baru)