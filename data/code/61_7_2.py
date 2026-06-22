import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == '__main__':
    sample_values = [2, 17, 18, 104729, 104730]
    for val in sample_values:
        print(is_prime(val))