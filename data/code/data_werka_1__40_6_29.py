class StringProcessor:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def first_letter_of_first_word(self):
        stripped_string = self.input_string.lstrip()
        if not stripped_string:
            raise ValueError("String is empty or contains only whitespace")
        
        first_space_index = stripped_string.find(' ')
        return stripped_string[0] if first_space_index == -1 else stripped_string[0]

if __name__ == '__main__':
    sample_string = '   Test string'
    processor = StringProcessor(sample_string)
    print(processor.first_letter_of_first_word())