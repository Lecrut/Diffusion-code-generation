class StringProcessor:
    def remove_spaces(self, input_string):
        return ''.join(input_string.split())

if __name__ == '__main__':
    processor = StringProcessor()
    sample_string = "This is a sample string with spaces"
    result = processor.remove_spaces(sample_string)
    print(result)