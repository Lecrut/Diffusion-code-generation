import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == '__main__':
    samples = [2, 3, 4, 17, 1000000007, 1000000009]
    results = [is_prime(n) for n in samples]
    for n, prime in zip(samples, results):
        print(f"{n}: {prime}")