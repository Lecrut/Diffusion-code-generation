class StringHandler:
    DEFAULT_STRINGS = ['watermelon', 'xigua', 'yam', 'zucchini']

    @staticmethod
    def print_first_letters(strings):
        for string in strings:
            if string:
                print(string[0])

if __name__ == '__main__':
    sample_strings = StringHandler.DEFAULT_STRINGS
    StringHandler.print_first_letters(sample_strings)