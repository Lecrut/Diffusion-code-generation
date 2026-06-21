def check_match(value1, value2):
    try:
        return value1 == value2
    except Exception as e:
        raise ValueError(f"Invalid input: {e}")

if __name__ == '__main__':
    sample_value1 = {"key": "value"}
    sample_value2 = {"key": "value"}
    result1 = check_match(sample_value1, sample_value2)
    print(result1)

    sample_value3 = (1, 2, 3)
    sample_value4 = (1, 2, 3)
    result2 = check_match(sample_value3, sample_value4)
    print(result2)

    sample_value5 = {"a": [1, 2], "b": [3, 4]}
    sample_value6 = {"a": [1, 2], "b": [3, 4]}
    result3 = check_match(sample_value5, sample_value6)
    print(result3)