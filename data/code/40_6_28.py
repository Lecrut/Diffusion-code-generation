class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def first_letter_of_first_word(self):
        if not self.input_string.strip():
            return None
        words = self.input_string.split()
        return words[0][0] if words else None

if __name__ == '__main__':
    processor = StringProcessor("Hello, World!")
    print(processor.first_letter_of_first_word())