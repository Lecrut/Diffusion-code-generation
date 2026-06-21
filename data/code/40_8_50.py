class StringProcessor:
    def __init__(self, strings):
        self.strings = strings

    def print_first_letters(self):
        for string in self.strings:
            if string:
                print(string[0])

    def get_first_letters(self):
        return [s[0] for s in self.strings if s]

if __name__ == '__main__':
    sample_strings = ['watermelon', 'xigua', 'yam', 'zucchini']
    processor = StringProcessor(sample_strings)
    processor.print_first_letters()
    first_letters = processor.get_first_letters()
    print(first_letters)