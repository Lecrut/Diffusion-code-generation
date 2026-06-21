class StringSplitter:
    DELIMITER = ' '

    @staticmethod
    def split_string_by_spaces(s):
        return s.split(StringSplitter.DELIMITER)

if __name__ == '__main__':
    sample_string = "Hello World This Is A Test"
    print(StringSplitter.split_string_by_spaces(sample_string))