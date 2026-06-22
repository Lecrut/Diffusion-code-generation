def validate_integer(value):
    if not isinstance(value, int):
        raise TypeError("Input must be an integer")

def add_large_integers(a: int, b: int) -> int:
    validate_integer(a)
    validate_integer(b)
    return a + b

if __name__ == '__main__':
    result = add_large_integers(12345678901234567890, 98765432109876543210)
    print(result)