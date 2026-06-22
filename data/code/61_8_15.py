import math

def _has_small_divisor(n, limit):
    if n % 2 == 0:
        return True
    if n % 3 == 0:
        return True
    step = 0
    start = 5
    while start + step <= limit:
        current = start + step
        if n % current == 0 or n % (current + 2) == 0:
            return True
        step += 6
    return False

def is_prime(n):
    if not isinstance(n, int):
        return False
    if n < 2:
        return False
    if n <= 3:
        return True
    limit = int(math.isqrt(n))
    if _has_small_divisor(n, limit):
        return False
    return True

if __name__ == '__main__':
    test_cases = [11, 13, 14, 15, 16, 17, 19, 20, 21, 23, 1000, 1009, 1000003]
    for value in test_cases:
        print(is_prime(value))