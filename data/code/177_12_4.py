class StringUtils:
    @staticmethod
    def split_string(input_string):
        return input_string.split()
if __name__ == '__main__':
    test_string1 = "this is a sample string"
    result1 = StringUtils.split_string(test_string1)
    print(f"'{test_string1}' split: {result1}")
    test_string2 = "  leading and trailing spaces   here"
    result2 = StringUtils.split_string(test_string2)
    print(f"'{test_string2}' split: {result2}")
    test_string3 = "singleword"
    result3 = StringUtils.split_string(test_string3)
    print(f"'{test_string3}' split: {result3}")
    test_string4 = ""
    result4 = StringUtils.split_string(test_string4)
    print(f"'{test_string4}' split: {result4}")