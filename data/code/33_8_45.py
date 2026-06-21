class StringCleaner:

    def clean(self, text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
        no_space_chars = [char for char in text if char != ' ']
        cleaned_text = ''.join(no_space_chars)
        return cleaned_text
if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_text = '  A new example with various spaces.  '
    cleaned_text = cleaner.clean(sample_text)
    print(cleaned_text)