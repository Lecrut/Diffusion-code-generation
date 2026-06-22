import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n == 3:
        return True
    if n % 3 == 0:
        return False
    limit = int(math.isqrt(n))
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    test_values = [0, 1, 2, 3, 4, 17, 18, 19, 20, 25, 29, 97, 100, 101]
    for val in test_values:
        result = is_prime(val)
        print(f"{val}: {result}")