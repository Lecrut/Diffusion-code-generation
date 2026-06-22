class StringCleaner:
    def clean(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return text.replace(" ", "")

if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_text = "  This is a sample text with spaces.  "
    cleaned_text = cleaner.clean(sample_text)
    print(cleaned_text)