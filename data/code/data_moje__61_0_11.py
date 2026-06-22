import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    sample_values = [2, 3, 4, 17, 18, 97, 98, 99, 100, 101]
    for val in sample_values:
        print(is_prime(val))