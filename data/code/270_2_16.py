class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def remove_spaces(self):
        return ''.join(char for char in self.input_string if char != ' ')

if __name__ == '__main__':
    processor = StringProcessor("Hello, World! This is a test.")
    print(processor.remove_spaces())