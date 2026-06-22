def validate_inputs(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")
    return True

def add_large_integers(a: int, b: int) -> int:
    validate_inputs(a, b)
    return a + b

if __name__ == '__main__':
    result = add_large_integers(12345678901234567890, 98765432109876543210)
    print(result)