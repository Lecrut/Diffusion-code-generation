def validate_inputs(value1, value2):
    if not isinstance(value1, (int, float)):
        raise ValueError("The first value must be an integer or float.")
    if not isinstance(value2, (int, float)):
        raise ValueError("The second value must be an integer or float.")

def determine_larger(value1, value2):
    validate_inputs(value1, value2)
    return max(value1, value2)

if __name__ == '__main__':
    sample_value1 = 99.9
    sample_value2 = 420
    larger_value = determine_larger(sample_value1, sample_value2)
    print(larger_value)