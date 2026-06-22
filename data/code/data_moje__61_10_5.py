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
    test_values = [0, 1, 2, 3, 4, 9, 17, 18, 25, 97, 100]
    for num in test_values:
        print(is_prime(num))