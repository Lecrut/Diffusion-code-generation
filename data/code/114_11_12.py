def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers (int or float)")

def multiply_numbers(a: int, b: int) -> int:
    validate_numbers(a, b)
    return a * b

if __name__ == '__main__':
    result = multiply_numbers(4, 3)
    print(result)