class StringSplitter:
    DELIMITER = ' '

    @staticmethod
    def split_string(input_string):
        return input_string.split(StringSplitter.DELIMITER)

if __name__ == '__main__':
    test_string = "split this string by spaces"
    result = StringSplitter.split_string(test_string)
    print(result)