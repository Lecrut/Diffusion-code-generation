class StringProcessor:
    DEFAULT_STRINGS = ['apple', 'banana', 'cherry', 'date']

    @staticmethod
    def print_first_letters(strings):
        for string in strings:
            if string:
                print(string[0])

if __name__ == '__main__':
    sample_strings = StringProcessor.DEFAULT_STRINGS
    StringProcessor.print_first_letters(sample_strings)