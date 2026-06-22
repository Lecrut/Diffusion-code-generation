class StringProcessor:
    def remove_spaces(self, input_string):
        return input_string.replace(' ', '')

if __name__ == '__main__':
    processor = StringProcessor()
    sample_string = 'Hello World! This is a test.'
    result = processor.remove_spaces(sample_string)
    print(result)