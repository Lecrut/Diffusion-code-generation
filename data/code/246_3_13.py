def validate_integer(value):
    if not isinstance(value, int):
        raise TypeError("Both inputs must be integers.")
    if value < 0:
        raise ValueError("Inputs must be non-negative.")

def add_large_integers(a: int, b: int) -> int:
    validate_integer(a)
    validate_integer(b)
    return a + b

if __name__ == '__main__':
    num1 = 98765432109876543210
    num2 = 12345678901234567890
    result = add_large_integers(num1, num2)
    print(result)