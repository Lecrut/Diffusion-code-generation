class StringCleaner:
    def clean(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return ''.join(filter(lambda c: c != ' ', text))

if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_text = "  This is another example with spaces.  "
    cleaned_text = cleaner.clean(sample_text)
    print(cleaned_text)