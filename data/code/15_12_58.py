def validate_exact_match(arg1, arg2):
    if arg1 is None or arg2 is None:
        return False
    return arg1 == arg2

if __name__ == '__main__':
    sample_value1 = "hello"
    sample_value2 = "hello"
    sample_value3 = 42
    sample_value4 = 42.0
    sample_value5 = [1, 2, 3]
    sample_value6 = [1, 2, 3]

    result1 = validate_exact_match(sample_value1, sample_value2)
    result2 = validate_exact_match(sample_value3, sample_value4)
    result3 = validate_exact_match(sample_value5, sample_value6)

    print(f"Result for string comparison: {result1}")
    print(f"Result for integer and float comparison: {result2}")
    print(f"Result for list comparison: {result3}")