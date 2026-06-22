import math

def fibonacci_binet(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    fib_n = (phi**n - psi**n) / sqrt5
    return int(round(fib_n))

def first_n_fibonacci(n):
    return [fibonacci_binet(i) for i in range(n)]

if __name__ == '__main__':
    result = first_n_fibonacci(80)
    print(result)