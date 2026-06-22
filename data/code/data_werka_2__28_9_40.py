def validate_inputs(value1, value2):
    if not isinstance(value1, (int, float)):
        raise ValueError("First value must be an integer or float")
    if not isinstance(value2, (int, float)):
        raise ValueError("Second value must be an integer or float")

def determine_larger(value1, value2):
    validate_inputs(value1, value2)
    return max(value1, value2)

if __name__ == '__main__':
    sample_value1 = 25.75
    sample_value2 = 100
    larger_value = determine_larger(sample_value1, sample_value2)
    print(larger_value)