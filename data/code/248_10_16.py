def validate_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers")
    if a < 0 or b < 0:
        raise ValueError("Both numbers must be non-negative")

def add_numbers(a: int, b: int) -> int:
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    num1 = 15
    num2 = 27
    result = add_numbers(num1, num2)
    print(result)