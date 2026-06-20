def validate_arguments(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError('Both arguments must be numeric')

def multiply_numbers(a: int, b: int) -> int:
    validate_arguments(a, b)
    return a * b
if __name__ == '__main__':
    result = multiply_numbers(4, 3)
    print(result)