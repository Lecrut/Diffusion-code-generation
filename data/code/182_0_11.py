class StringSeparator:
    SEPARATOR = '-'

    @staticmethod
    def separate_characters(input_string):
        return StringSeparator.SEPARATOR.join([char for char in input_string])

if __name__ == '__main__':
    sample_string = "HelloWorld"
    result = StringSeparator.separate_characters(sample_string)
    print(result)