from math import sqrt
from decimal import Decimal, getcontext

def compute_fibonacci_binet(n):
    getcontext().prec = 100
    sqrt5 = Decimal(5).sqrt()
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    fib_n = (phi ** n - psi ** n) / sqrt5
    return int(fib_n.to_integral_value(rounding='ROUND_HALF_UP'))

if __name__ == '__main__':
    fibs = [compute_fibonacci_binet(i) for i in range(80)]
    print(fibs)