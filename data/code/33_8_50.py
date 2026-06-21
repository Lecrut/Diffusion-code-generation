class StringCleaner:
    def clean(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return ''.join(c for c in text if c != ' ')

if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_text = "  This is a sample text with spaces.  "
    cleaned_text = cleaner.clean(sample_text)
    print(cleaned_text)