def _validate_number(n):
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number")
    return True

def is_even(n):
    _validate_number(n)
    return int(n) % 2 == 0

if __name__ == '__main__':
    print(is_even(4))
    print(is_even(7))
    print(is_even(0))
    print(is_even(-3))
    print(is_even(-2))