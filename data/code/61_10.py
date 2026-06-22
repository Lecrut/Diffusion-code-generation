import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    test_values = [0, 1, 2, 3, 4, 17, 18, 97, 100, 7919, 8000]
    for value in test_values:
        print(f"{value}: {is_prime(value)}")