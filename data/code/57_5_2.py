import math

def binet_fibonacci(n):
    if n <= 1:
        return n
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    result = (phi**n - psi**n) / math.sqrt(5)
    return int(round(result))

if __name__ == '__main__':
    for i in range(80):
        print(binet_fibonacci(i))