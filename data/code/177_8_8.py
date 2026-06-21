class StringSplitter:
    DEFAULT_DELIMITER = ' '

    @staticmethod
    def split_text(input_string):
        return input_string.split(StringSplitter.DEFAULT_DELIMITER)

if __name__ == '__main__':
    splitter = StringSplitter()
    sample1 = "hello world"
    result1 = splitter.split_text(sample1)
    print(f"Input: '{sample1}'")
    print(f"Output: {result1}")

    sample2 = "  leading and trailing spaces "
    result2 = splitter.split_text(sample2)
    print(f"Input: '{sample2}'")
    print(f"Output: {result2}")

    sample3 = "singleword"
    result3 = splitter.split_text(sample3)
    print(f"Input: '{sample3}'")
    print(f"Output: {result3}")

    sample4 = ""
    result4 = splitter.split_text(sample4)
    print(f"Input: '{sample4}'")
    print(f"Output: {result4}")