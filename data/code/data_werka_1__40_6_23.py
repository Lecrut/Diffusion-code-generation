class StringProcessor:

    def __init__(self, input_string):
        self.input_string = input_string

    def get_first_letter_of_first_word(self):
        stripped_string = self.input_string.lstrip()
        first_space_index = stripped_string.find(' ')
        if first_space_index == -1:
            return stripped_string[0]
        else:
            return stripped_string[0]
if __name__ == '__main__':
    sample_string = '   Hello World'
    processor = StringProcessor(sample_string)
    print(processor.get_first_letter_of_first_word())