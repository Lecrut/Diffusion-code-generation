def validate_inputs(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be integers or floats")

def compare_two_simple_quantities_now_transform(a, b):
    validate_inputs(a, b)
    return a > b

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_transform(5, 3)
    print(result)