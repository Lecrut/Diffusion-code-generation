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
    test_cases = [0, 1, 2, 3, 4, 5, 10, 13, 17, 18, 20, 97, 100]
    results = []
    for number in test_cases:
        result = is_prime(number)
        results.append((number, result))
    for number, result in results:
        print(f"{number}: {result}")