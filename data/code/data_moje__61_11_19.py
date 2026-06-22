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
    test_values = [2, 3, 4, 5, 16, 17, 18, 19, 23, 24, 25, 49, 97, 100, 101, 541]
    for value in test_values:
        print(f"{value}: {is_prime(value)}")