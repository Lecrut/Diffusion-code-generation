def _validate_int(value):
    if not isinstance(value, int):
        raise TypeError("Input must be an integer")
    return value

def is_even(n):
    _validate_int(n)
    return (n & 1) == 0

if __name__ == '__main__':
    print(is_even(10))
    print(is_even(7))
    print(is_even(0))
    print(is_even(-5))