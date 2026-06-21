def _validate_types(arg1, arg2):
    if not isinstance(arg1, type(arg2)):
        raise ValueError("Arguments must be of the same type")

def validate_exact_match(arg1, arg2):
    _validate_types(arg1, arg2)
    return arg1 == arg2

if __name__ == '__main__':
    try:
        sample_value1 = "hello"
        sample_value2 = "hello"
        result1 = validate_exact_match(sample_value1, sample_value2)
        
        sample_value3 = 42.0
        sample_value4 = 42
        result2 = validate_exact_match(sample_value3, sample_value4)
        
        print(f"Result for string comparison: {result1}")
        print(f"Result for numeric comparison: {result2}")
    except ValueError as e:
        print(e)