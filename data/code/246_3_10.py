def validate_input(a: int, b: int) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    return True

def add_large_integers(a: int, b: int) -> int:
    if not validate_input(a, b):
        return None
    return a + b

if __name__ == '__main__':
    num1 = 98765432109876543210
    num2 = 12345678901234567890
    result = add_large_integers(num1, num2)
    print(result)