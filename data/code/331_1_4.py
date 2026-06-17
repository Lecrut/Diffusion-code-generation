def to_lower_string(input_string):
    return input_string.lower()
if __name__ == '__main__':
    test_string_1 = "HeLlO WoRlD"
    result_1 = to_lower_string(test_string_1)
    print(f"Input: {test_string_1}")
    print(f"Output: {result_1}")
    test_string_2 = "PYTHON 3.10"
    result_2 = to_lower_string(test_string_2)
    print(f"Input: {test_string_2}")
    print(f"Output: {result_2}")
    test_string_3 = "already_lower"
    result_3 = to_lower_string(test_string_3)
    print(f"Input: {test_string_3}")
    print(f"Output: {result_3}")