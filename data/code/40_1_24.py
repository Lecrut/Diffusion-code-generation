class TextProcessor:
    def __init__(self, text):
        self.text = text

    def get_first_letters(self):
        return [word[0] for word in self.text.split()]

if __name__ == '__main__':
    sample_string_1 = "This is an example string"
    processor_1 = TextProcessor(sample_string_1)
    print(processor_1.get_first_letters())

    sample_string_2 = "Another test case here"
    processor_2 = TextProcessor(sample_string_2)
    print(processor_2.get_first_letters())