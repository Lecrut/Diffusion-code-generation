class StringProcessor:
    @staticmethod
    def remove_spaces(input_string):
        return input_string.replace(' ', '')

if __name__ == '__main__':
    sample_input = '  This is   an example string with multiple spaces.  '
    processor = StringProcessor()
    result = processor.remove_spaces(sample_input)
    print(result)