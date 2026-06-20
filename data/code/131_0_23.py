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

def validate_number(n):
    try:
        number = int(n)
        return number
    except ValueError:
        raise ValueError("Input must be a valid integer")

if __name__ == '__main__':
    test_cases = [2, 3, 4, 5, 17, 18, 19, 20, 23, 29, 31]
    for num in test_cases:
        try:
            number = validate_number(num)
            print(f"{number} is prime: {is_prime(number)}")
        except ValueError as e:
            print(e)