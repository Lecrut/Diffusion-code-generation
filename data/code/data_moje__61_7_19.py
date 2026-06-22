import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    limit = math.isqrt(n)
    while i <= limit:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

if __name__ == '__main__':
    print(is_prime(2))
    print(is_prime(17))
    print(is_prime(1000000007))
    print(is_prime(1000000000039))