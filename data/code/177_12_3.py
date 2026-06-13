class StringUtils:
    @staticmethod
    def split_string_by_space(input_string):
        return input_string.split()
if __name__ == '__main__':
    test_string_1 = "this is a sample string"
    result_1 = StringUtils.split_string_by_space(test_string_1)
    print(f"Input: '{test_string_1}'")
    print(f"Output: {result_1}")
    test_string_2 = "  leading and trailing spaces   in between "
    result_2 = StringUtils.split_string_by_space(test_string_2)
    print(f"Input: '{test_string_2}'")
    print(f"Output: {result_2}")
    test_string_3 = "singleword"
    result_3 = StringUtils.split_string_by_space(test_string_3)
    print(f"Input: '{test_string_3}'")
    print(f"Output: {result_3}")
    test_string_4 = ""
    result_4 = StringUtils.split_string_by_space(test_string_4)
    print(f"Input: '{test_string_4}'")
    print(f"Output: {result_4}")