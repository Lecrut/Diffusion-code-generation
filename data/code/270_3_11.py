class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def remove_spaces(self):
        return self.input_string.replace(' ', '')

if __name__ == '__main__':
    processor = StringProcessor("  Hello World!  ")
    result = processor.remove_spaces()
    print(result)