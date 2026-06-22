import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == '__main__':
    test_values = [2, 17, 18, 7919, 1000000007, 1000000007 * 2, 15]
    for val in test_values:
        result = is_prime(val)
        print(f"is_prime({val}) = {result}")