def check_match(value1, value2):
    equality_map = {
        True: True,
        False: False
    }
    return equality_map.get(value1 == value2)

if __name__ == '__main__':
    sample_value1 = {"key": "value"}
    sample_value2 = {"key": "value"}
    result = check_match(sample_value1, sample_value2)
    print(result)