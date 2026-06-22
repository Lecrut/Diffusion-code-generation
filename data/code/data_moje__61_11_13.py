import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_prime_alternative(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def test_prime_checker():
    test_cases = [(2, True), (3, True), (4, False), (17, True), (18, False), (19, True), (20, False), (97, True), (100, False), (1, False), (0, False), (-5, False), (7919, True), (7920, False)]
    results = []
    for n, expected in test_cases:
        result = is_prime(n)
        results.append((n, expected, result, result == expected))
    return results
if __name__ == '__main__':
    results = test_prime_checker()
    for n, expected, actual, passed in results:
        print(f'n={n}, expected={expected}, actual={actual}, passed={passed}')