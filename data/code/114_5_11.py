def validate_input(a):
    if not isinstance(a, (int, float)):
        raise ValueError("Input must be numeric")

def multiply_numbers(a: float, b: float) -> float:
    validate_input(a)
    validate_input(b)
    return a * b

if __name__ == '__main__':
    result = multiply_numbers(3.5, 2.0)
    print(result)