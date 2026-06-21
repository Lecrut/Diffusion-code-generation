def validate_inputs(value1, value2):
    if not isinstance(value1, type(value2)):
        raise ValueError("Inputs must be of the same type")

def check_match(value1, value2):
    validate_inputs(value1, value2)
    return value1 == value2

if __name__ == '__main__':
    sample_value1 = 42
    sample_value2 = 42
    result = check_match(sample_value1, sample_value2)
    print(result)