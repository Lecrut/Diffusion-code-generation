def check_match(value1, value2):
    try:
        return value1 == value2
    except Exception as e:
        raise ValueError(f"Invalid input: {e}")

if __name__ == '__main__':
    sample_value1 = {"key": "value"}
    sample_value2 = {"key": "value"}
    result = check_match(sample_value1, sample_value2)
    print(result)