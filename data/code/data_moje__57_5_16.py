def fibonacci(n):
    sqrt5 = 5 ** 0.5
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    return round((phi ** n - psi ** n) / sqrt5)

if __name__ == '__main__':
    for i in range(80):
        print(fibonacci(i))