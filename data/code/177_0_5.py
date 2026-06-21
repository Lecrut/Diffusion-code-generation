class StringSplitter:
    WHITESPACE_DELIMITERS = ' \t\n\r\f\v'

    @staticmethod
    def split_string_by_spaces(s):
        return s.split(StringSplitter.WHITESPACE_DELIMITERS)

if __name__ == '__main__':
    sample_string = "Hello World This Is A Test"
    splitter = StringSplitter()
    print(splitter.split_string_by_spaces(sample_string))