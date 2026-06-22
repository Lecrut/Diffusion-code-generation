class StringProcessor:
    EMPTY_STRING_ERROR = "Input string cannot be empty"

    @staticmethod
    def get_first_letter(s):
        if not s:
            raise ValueError(StringProcessor.EMPTY_STRING_ERROR)
        return s[0]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    first_letter = StringProcessor.get_first_letter(sample_string)
    print(first_letter)