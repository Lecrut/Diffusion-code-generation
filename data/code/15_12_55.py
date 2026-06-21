def _is_same_type(arg1, arg2):
    return isinstance(arg1, type(arg2))

def validate_exact_match(arg1, arg2):
    if not _is_same_type(arg1, arg2):
        raise ValueError("Arguments must be of the same type")
    return arg1 == arg2

if __name__ == '__main__':
    sample_value1 = 3.14
    sample_value2 = 3.14
    sample_value3 = "hello"
    sample_value4 = "world"
    sample_value5 = [1, 2, 3]
    sample_value6 = [1, 2, 3]

    try:
        result1 = validate_exact_match(sample_value1, sample_value2)
        result2 = validate_exact_match(sample_value3, sample_value4)
        result3 = validate_exact_match(sample_value5, sample_value6)
        print(f"Result for float comparison: {result1}")
        print(f"Result for string comparison: {result2}")
        print(f"Result for list comparison: {result3}")
    except ValueError as e:
        print(e)