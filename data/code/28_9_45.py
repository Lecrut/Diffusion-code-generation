def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Both values must be integers or floats")

def determine_larger(value1, value2):
    validate_input(value1)
    validate_input(value2)
    return max(value1, value2)

if __name__ == '__main__':
    sample_value1 = 5.67
    sample_value2 = 89
    larger_value = determine_larger(sample_value1, sample_value2)
    print(larger_value)