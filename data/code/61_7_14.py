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
    test_values = [2, 3, 4, 17, 18, 97, 98, 99, 100, 101, 7919, 8000]
    results = [(val, is_prime(val)) for val in test_values]
    for val, result in results:
        print(f"{val}: {result}")