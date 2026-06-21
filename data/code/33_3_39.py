class StringFilter:
    ALPHANUMERIC_PATTERN = '[^a-zA-Z0-9]'

    @staticmethod
    def filter_alphanumeric(input_string):
        return re.sub(StringFilter.ALPHANUMERIC_PATTERN, '', input_string)

if __name__ == '__main__':
    sample_input = 'Hello, World! 123.'
    result = StringFilter.filter_alphanumeric(sample_input)
    print(result)