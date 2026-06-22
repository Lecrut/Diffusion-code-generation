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

def validate_input(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")

if __name__ == '__main__':
    try:
        validate_input(29)
        print(is_prime(29))
    except ValueError as e:
        print(e)

    try:
        validate_input(15)
        print(is_prime(15))
    except ValueError as e:
        print(e)