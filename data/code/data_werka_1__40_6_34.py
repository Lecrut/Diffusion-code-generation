class StringProcessor:

    def __init__(self, text):
        self.text = text

    def first_letter_of_first_word(self):
        stripped_text = self.text.lstrip()
        if not stripped_text:
            return None
        first_space_index = stripped_text.find(' ')
        if first_space_index == -1:
            return stripped_text[0]
        else:
            return stripped_text[0]
if __name__ == '__main__':
    sample_text = '  Hello, world!'
    processor = StringProcessor(sample_text)
    print(processor.first_letter_of_first_word())