class StringCleaner:

    def clean(self, text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')

        def is_valid_string(s):
            return isinstance(s, str)

        def remove_spaces(s):
            return ''.join((char for char in s if char != ' '))
        if not is_valid_string(text):
            raise ValueError('Input must be a string')
        cleaned_text = remove_spaces(text)
        return cleaned_text
if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_text = '  This is a unique example with spaces.  '
    cleaned_text = cleaner.clean(sample_text)
    print(cleaned_text)