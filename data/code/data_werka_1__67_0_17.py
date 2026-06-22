def validate_numbers(a, b):
    if not isinstance(a, (int, float)):
        raise ValueError(f"First argument must be an integer or float, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise ValueError(f"Second argument must be an integer or float, got {type(b).__name__}")

def sum_two_numbers(a, b):
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    try:
        result = sum_two_numbers(123, 456)
        print(result)
    except ValueError as e:
        print(e)