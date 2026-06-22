def validate_input(a: int, b: int) -> None:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")

def add_large_integers(a: int, b: int) -> int:
    validate_input(a, b)
    return a + b

if __name__ == '__main__':
    result1 = add_large_integers(5, 3)
    print(result1)
    num1 = 98765432109876543210
    num2 = 12345678901234567890
    result2 = add_large_integers(num1, num2)
    print(result2)