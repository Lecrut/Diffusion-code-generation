def to_lower_string(input_string):
    return input_string.lower()
if __name__ == '__main__':
    test_string_1 = "HeLlO WoRlD"
    result_1 = to_lower_string(test_string_1)
    print(f"Input: {test_string_1}, Output: {result_1}")
    test_string_2 = "PYTHON"
    result_2 = to_lower_string(test_string_2)
    print(f"Input: {test_string_2}, Output: {result_2}")
    test_string_3 = "already lowercase"
    result_3 = to_lower_string(test_string_3)
    print(f"Input: {test_string_3}, Output: {result_3}")
    test_string_4 = "123!@#"
    result_4 = to_lower_string(test_string_4)
    print(f"Input: {test_string_4}, Output: {result_4}")