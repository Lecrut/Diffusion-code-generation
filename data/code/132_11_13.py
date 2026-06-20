def validate_number(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n

def is_even(n):
    n = validate_number(n)
    return n & 1 == 0

if __name__ == '__main__':
    print(is_even(4))
    print(is_even(5))
    print(is_even(0))
    print(is_even(-2))
    print(is_even(-3))