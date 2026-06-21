def validate_input(value):
    if value is None:
        raise ValueError("Input values cannot be None")
    return value

def check_match(value1, value2):
    validated_value1 = validate_input(value1)
    validated_value2 = validate_input(value2)
    return validated_value1 == validated_value2

if __name__ == '__main__':
    sample_value1 = {"key": "value"}
    sample_value2 = {"key": "value"}
    result = check_match(sample_value1, sample_value2)
    print(result)