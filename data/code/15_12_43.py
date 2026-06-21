def validate_exact_match(arg1, arg2):
    if not isinstance(arg1, type(arg2)):
        raise ValueError("Arguments must be of the same type")
    return _compare_values(arg1, arg2)

def _compare_values(value1, value2):
    return value1 == value2

if __name__ == '__main__':
    try:
        sample_value1 = "hello"
        sample_value2 = "world"
        result1 = validate_exact_match(sample_value1, sample_value2)
        
        sample_value3 = [1, 2, 3]
        sample_value4 = [1, 2, 3]
        result2 = validate_exact_match(sample_value3, sample_value4)
        
        sample_value5 = 3.14
        sample_value6 = 3.14
        result3 = validate_exact_match(sample_value5, sample_value6)
        
        print(f"Result for string comparison: {result1}")
        print(f"Result for list comparison: {result2}")
        print(f"Result for float comparison: {result3}")
    except ValueError as e:
        print(e)