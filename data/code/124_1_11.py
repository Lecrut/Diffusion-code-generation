def validate_inputs(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return True

def basic_arithmetic(a, b):
    validate_inputs(a, b)
    return {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'floor_division': a // b
    }

if __name__ == '__main__':
    result = basic_arithmetic(10, 4)
    print(result)