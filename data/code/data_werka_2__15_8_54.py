def check_match(value1, value2):
    comparison_results = {
        True: True,
        False: False
    }
    try:
        return comparison_results[value1 == value2]
    except Exception as e:
        raise ValueError(f"Invalid input: {e}")

if __name__ == '__main__':
    sample_value1 = {'a': 1, 'b': 2}
    sample_value2 = {'a': 1, 'b': 2}
    result = check_match(sample_value1, sample_value2)
    print(result)