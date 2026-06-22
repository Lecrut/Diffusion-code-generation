class StringCleaner:
    SPACE_CHARACTER = ' '

    def clean(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return ''.join(char for char in text if char != self.SPACE_CHARACTER)

if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_text = "  This is a unique example with spaces.  "
    cleaned_text = cleaner.clean(sample_text)
    print(cleaned_text)