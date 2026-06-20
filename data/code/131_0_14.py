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
if __name__ == '__main__':
    print(is_prime(2))
    print(is_prime(3))
    print(is_prime(4))
    print(is_prime(17))
    print(is_prime(18))