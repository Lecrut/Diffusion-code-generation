def validate_exact_match(arg1, arg2):
    if not isinstance(arg1, type(arg2)):
        raise ValueError("Arguments must be of the same type")
    return arg1 == arg2

if __name__ == '__main__':
    try:
        sample_value1 = (1, 2, 3)
        sample_value2 = (1, 2, 3)
        result1 = validate_exact_match(sample_value1, sample_value2)
        
        sample_value3 = {"key": "value"}
        sample_value4 = {"key": "value"}
        result2 = validate_exact_match(sample_value3, sample_value4)
        
        print(f"Result for tuple comparison: {result1}")
        print(f"Result for dictionary comparison: {result2}")
    except ValueError as e:
        print(e)