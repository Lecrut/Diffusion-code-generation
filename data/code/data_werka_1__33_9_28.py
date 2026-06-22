class StringCleaner:

    def clean(self, text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
        return ''.join(text.split())
if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_text = '  This is   a   test string.  '
    cleaned_text = cleaner.clean(sample_text)
    print(cleaned_text)