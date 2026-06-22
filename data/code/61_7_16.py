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
    sample_values = [2, 3, 17, 25, 97, 100, 104729]
    results = [(val, is_prime(val)) for val in sample_values]
    for val, prime in results:
        print(f"{val} is {'prime' if prime else 'not prime'}")