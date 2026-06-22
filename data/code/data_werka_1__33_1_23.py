class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def remove_spaces(self):
        return ''.join(char for char in self.input_string if char != ' ')

if __name__ == '__main__':
    sample_input = "Hello World from Alibaba Cloud"
    processor = StringProcessor(sample_input)
    result = processor.remove_spaces()
    print(result)