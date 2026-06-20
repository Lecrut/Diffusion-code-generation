def validate_numeric(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be numeric")

def multiply_numbers(a: float, b: float) -> float:
    validate_numeric(a)
    validate_numeric(b)
    return a * b

if __name__ == '__main__':
    result = multiply_numbers(3.5, 2.0)
    print(result)