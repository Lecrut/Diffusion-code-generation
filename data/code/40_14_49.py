class StringProcessor:
    def __init__(self, input_string):
        if not isinstance(input_string, str) or not input_string:
            raise ValueError("Input must be a non-empty string")
        self.input_string = input_string

    def get_first_letter(self):
        return self.input_string[0]

if __name__ == '__main__':
    sample_string1 = "Hello, World!"
    processor1 = StringProcessor(sample_string1)
    print(processor1.get_first_letter())

    sample_string2 = "Alibaba Cloud"
    processor2 = StringProcessor(sample_string2)
    print(processor2.get_first_letter())