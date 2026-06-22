from decimal import Decimal, getcontext

def fibonacci_binet(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    getcontext().prec = max(50, n * 5)
    sqrt5 = Decimal(5).sqrt()
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    fib_n = (phi ** n - psi ** n) / sqrt5
    return int(round(fib_n))

if __name__ == '__main__':
    for i in range(80):
        print(fibonacci_binet(i))