class StringProcessor:
    INPUT_ERROR_MESSAGE = "Input must be a non-empty string"

    @staticmethod
    def get_first_letter(s):
        if not isinstance(s, str) or not s:
            raise ValueError(StringProcessor.INPUT_ERROR_MESSAGE)
        return s[0]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    first_letter = StringProcessor.get_first_letter(sample_string)
    print(first_letter)