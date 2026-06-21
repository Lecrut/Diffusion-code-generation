def check_match(value1, value2):
    def validate_inputs(val1, val2):
        if not isinstance(val1, type(val2)):
            raise ValueError("Inputs must be of the same type")
    
    try:
        validate_inputs(value1, value2)
        return value1 == value2
    except ValueError as e:
        print(f"Validation error: {e}")
        return False

if __name__ == '__main__':
    sample_value1 = {"key": "value"}
    sample_value2 = {"key": "value"}
    result = check_match(sample_value1, sample_value2)
    print(result)