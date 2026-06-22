import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    test_values = [0, 1, 2, 3, 4, 5, 16, 17, 20, 97, 100, 101]
    results = [is_prime(v) for v in test_values]
    print(results)