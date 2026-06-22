class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def remove_spaces(self):
        result = ''.join(char for char in self.input_string if char != ' ')
        return result

if __name__ == '__main__':
    sample_input = "Hello World This is a Test"
    processor = StringProcessor(sample_input)
    print(processor.remove_spaces())