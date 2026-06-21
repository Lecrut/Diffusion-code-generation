class StringProcessor:
    def __init__(self, input_string):
        if not isinstance(input_string, str) or not input_string:
            raise ValueError("Input must be a non-empty string")
        self.input_string = input_string

    def get_first_letter(self):
        return self.input_string[0]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    processor = StringProcessor(sample_string)
    print(processor.get_first_letter())