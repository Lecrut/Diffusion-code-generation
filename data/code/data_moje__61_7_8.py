import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    sample_values = [2, 3, 4, 17, 18, 97, 100, 104729]
    for val in sample_values:
        print(is_prime(val))