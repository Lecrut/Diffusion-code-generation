class StringSplitter:
    @staticmethod
    def split_string(input_string):
        return input_string.split()

if __name__ == '__main__':
    splitter = StringSplitter()
    test_string1 = "this is a sample string"
    result1 = splitter.split_string(test_string1)
    print(f"Input: '{test_string1}'")
    print(f"Output: {result1}")
    test_string2 = "  leading and trailing spaces   in between "
    result2 = splitter.split_string(test_string2)
    print(f"Input: '{test_string2}'")
    print(f"Output: {result2}")
    test_string3 = "singleword"
    result3 = splitter.split_string(test_string3)
    print(f"Input: '{test_string3}'")
    print(f"Output: {result3}")
    test_string4 = ""
    result4 = splitter.split_string(test_string4)
    print(f"Input: '{test_string4}'")
    print(f"Output: {result4}")