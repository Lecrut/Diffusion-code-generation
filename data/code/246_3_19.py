def validate_numeric_input(value):
    if not isinstance(value, int):
        raise TypeError("Input must be an integer")

def add_large_integers(a: int, b: int) -> int:
    validate_numeric_input(a)
    validate_numeric_input(b)
    return a + b

if __name__ == '__main__':
    result1 = add_large_integers(5, 3)
    print(result1)
    
    num1 = 98765432109876543210
    num2 = 12345678901234567890
    result2 = add_large_integers(num1, num2)
    print(result2)