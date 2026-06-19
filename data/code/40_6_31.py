class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def is_non_empty(self):
        return bool(self.input_string.strip())

    def first_letter_of_first_word(self):
        if not self.is_non_empty():
            return None
        stripped_string = self.input_string.lstrip()
        first_space_index = stripped_string.find(' ')
        if first_space_index == -1:
            return stripped_string[0]
        else:
            return stripped_string[0]

if __name__ == '__main__':
    sample_string = '   Welcome to the world'
    processor = StringProcessor(sample_string)
    print(processor.first_letter_of_first_word())