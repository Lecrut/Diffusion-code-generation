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
    test_cases = [2, 3, 4, 5, 10, 17, 18, 19, 97, 98, 99, 100]
    for num in test_cases:
        result = is_prime(num)
        print(f"{num}: {result}")