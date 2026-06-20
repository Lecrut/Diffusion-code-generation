def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError('Input must be a number')

def subtract_numbers(a, b):
    validate_input(a)
    validate_input(b)
    return float(a - b)

if __name__ == '__main__':
    result = subtract_numbers(10, 5)
    print(result)