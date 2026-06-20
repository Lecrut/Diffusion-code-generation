import math
THRESHOLD = 2

def is_prime(n):
    if n <= THRESHOLD:
        return n > 1
    if n % 2 == 0:
        return False
    max_divisor = int(math.sqrt(n)) + 1
    for divisor in range(3, max_divisor, 2):
        if n % divisor == 0:
            return False
    return True
if __name__ == '__main__':
    test_cases = [2, 3, 4, 5, 17, 18, 19, 20, 23, 29, 31]
    for num in test_cases:
        print(f'{num} is prime: {is_prime(num)}')