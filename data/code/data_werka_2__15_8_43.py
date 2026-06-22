def check_match(value1, value2):
    equality_mapping = {
        True: True,
        False: False
    }
    return equality_mapping.get(value1 == value2, False)

if __name__ == '__main__':
    sample_value1 = {"a": 1, "b": 2}
    sample_value2 = {"a": 1, "b": 2}
    result = check_match(sample_value1, sample_value2)
    print(result)