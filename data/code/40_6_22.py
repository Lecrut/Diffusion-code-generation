class StringProcessor:

    def __init__(self, input_string):
        self.input_string = input_string

    def first_letter_of_first_word(self):
        stripped_string = self.input_string.lstrip()
        if ' ' in stripped_string:
            return stripped_string[0]
        else:
            return stripped_string[0] if stripped_string else None
if __name__ == '__main__':
    sample_string = '   Example text'
    processor = StringProcessor(sample_string)
    print(processor.first_letter_of_first_word())