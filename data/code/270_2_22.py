class StringProcessor:
    @staticmethod
    def remove_spaces(input_string):
        return ''.join(char for char in input_string if char != ' ')

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test."
    processor = StringProcessor()
    print(processor.remove_spaces(sample_string))