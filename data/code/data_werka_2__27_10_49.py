def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or a float.")

def are_values_different(a, b):
    validate_input(a)
    validate_input(b)
    return abs(a - b) > 1e-10

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    result = are_values_different(value1, value2)
    print(result)