class StringSeparator:
    SEPARATOR = ', '

    @staticmethod
    def separate_characters(input_string):
        return StringSeparator.SEPARATOR.join(input_string)

if __name__ == '__main__':
    sample_string = "Hello World"
    result = StringSeparator.separate_characters(sample_string)
    print(result)