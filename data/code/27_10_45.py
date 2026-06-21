def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both values must be either int or float.")

def are_values_different(a, b, epsilon=1e-10):
    validate_numbers(a, b)
    return abs(a - b) > epsilon

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    result = are_values_different(value1, value2)
    print(result)