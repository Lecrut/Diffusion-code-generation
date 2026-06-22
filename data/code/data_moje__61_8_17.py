import math

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(math.isqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

if __name__ == '__main__':
    test_values = [0, 1, 2, 3, 4, 17, 18, 97, 99, 100, 101, 7919]
    for val in test_values:
        print(f"{val}: {is_prime(val)}")