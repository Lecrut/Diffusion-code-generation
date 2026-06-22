class StringProcessor:
    def __init__(self, strings):
        self.strings = strings

    def print_first_letters(self):
        for string in self.strings:
            if string:
                print(string[0])

if __name__ == '__main__':
    sample_strings = ['kiwi', 'mango', 'nectarine', 'orange']
    processor = StringProcessor(sample_strings)
    processor.print_first_letters()