def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")

def check_difference(a, b):
    validate_numbers(a, b)
    return a != b

if __name__ == '__main__':
    sample_value1 = 42.0
    sample_value2 = 42.0001
    result = check_difference(sample_value1, sample_value2)
    print(result)