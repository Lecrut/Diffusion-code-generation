import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n == 3:
        return True
    if n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    test_values = [0, 1, 2, 3, 4, 5, 17, 18, 19, 20, 25, 29, 97, 100, 101, 0.5, -5, 49, 51, 9733]
    for val in test_values:
        if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
            int_val = int(val)
            result = is_prime(int_val)
            print(f"is_prime({int_val}) = {result}")
        else:
            print(f"is_prime({val}) = False")