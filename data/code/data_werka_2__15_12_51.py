def is_same_type(arg1, arg2):
    return type(arg1) == type(arg2)

def validate_exact_match(arg1, arg2):
    if not is_same_type(arg1, arg2):
        raise ValueError("Arguments must be of the same type")
    return arg1 == arg2

if __name__ == '__main__':
    try:
        sample_value1 = 42
        sample_value2 = 42
        result1 = validate_exact_match(sample_value1, sample_value2)
        print(f"Result for integer comparison: {result1}")

        sample_value3 = "hello"
        sample_value4 = "world"
        result2 = validate_exact_match(sample_value3, sample_value4)
        print(f"Result for string comparison: {result2}")

        sample_value5 = [1, 2, 3]
        sample_value6 = [1, 2, 3]
        result3 = validate_exact_match(sample_value5, sample_value6)
        print(f"Result for list comparison: {result3}")

    except ValueError as e:
        print(e)