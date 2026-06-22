import math

def fibonacci_binet(n: int) -> int:
    if n < 0:
        raise ValueError("Index must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    val = (phi ** n - psi ** n) / math.sqrt(5)
    return round(val)

if __name__ == '__main__':
    for i in range(80):
        print(fibonacci_binet(i))