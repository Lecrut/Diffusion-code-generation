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
    test_values = [0, 1, 2, 3, 4, 17, 18, 97, 100, 997, 999999937, 999999938]
    results = [is_prime(val) for val in test_values]
    for val, result in zip(test_values, results):
        print(f"{val}: {result}")