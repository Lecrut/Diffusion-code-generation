class StringHandler:
    DEFAULT_STRINGS = ['watermelon', 'xigua', 'yam', 'zucchini']

    @staticmethod
    def extract_first_letters(strings):
        if not isinstance(strings, list):
            raise ValueError("Input must be a list of strings.")
        return [s[0] for s in strings if s]

if __name__ == '__main__':
    sample_strings = StringHandler.DEFAULT_STRINGS
    try:
        first_letters = StringHandler.extract_first_letters(sample_strings)
        print(first_letters)
    except ValueError as e:
        print(e)