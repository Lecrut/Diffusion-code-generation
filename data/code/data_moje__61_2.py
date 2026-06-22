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
    test_numbers = [0, 1, 2, 3, 4, 5, 17, 25, 29, 97, 100]
    results = {num: is_prime(num) for num in test_numbers}
    print(results)