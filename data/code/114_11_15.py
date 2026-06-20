def validate_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be numbers")

def product(a: int | float, b: int | float) -> int | float:
    validate_numbers(a, b)
    return a * b

if __name__ == '__main__':
    num1 = 3.14159
    num2 = 2.71828
    result = product(num1, num2)
    print(result)