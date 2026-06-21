class StringSplitter:
    DELIMITER = ' '

    @staticmethod
    def split_and_filter(text):
        parts = text.split(StringSplitter.DELIMITER)
        filtered_parts = [part for part in parts if part]
        return filtered_parts

if __name__ == '__main__':
    splitter = StringSplitter()
    sample1 = "this is a test"
    result1 = splitter.split_and_filter(sample1)
    print(f"Input: '{sample1}'")
    print(f"Output: {result1}")
    sample2 = "  leading and trailing spaces "
    result2 = splitter.split_and_filter(sample2)
    print(f"Input: '{sample2}'")
    print(f"Output: {result2}")
    sample3 = "singleword"
    result3 = splitter.split_and_filter(sample3)
    print(f"Input: '{sample3}'")
    print(f"Output: {result3}")
    sample4 = "   "
    result4 = splitter.split_and_filter(sample4)
    print(f"Input: '{sample4}'")
    print(f"Output: {result4}")