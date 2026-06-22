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
    sample_values = [0, 1, 2, 17, 18, 19, 25, 29, 31, 97, 100, 101]
    results = [is_prime(val) for val in sample_values]
    print(list(zip(sample_values, results)))