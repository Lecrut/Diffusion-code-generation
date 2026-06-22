import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(math.isqrt(n))
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    sample_numbers = [2, 3, 4, 5, 17, 18, 19, 97, 100, 101, 104729, 104730]
    for num in sample_numbers:
        result = is_prime(num)
        print(f"{num}: {result}")