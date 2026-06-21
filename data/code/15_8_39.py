def check_match(value1, value2):
    match_results = {
        True: True,
        False: False
    }
    return match_results[value1 == value2]

if __name__ == '__main__':
    sample_value1 = "hello"
    sample_value2 = "hello"
    result = check_match(sample_value1, sample_value2)
    print(result)