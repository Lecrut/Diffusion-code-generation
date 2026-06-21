class StringCleaner:
    SPACE_CHAR = ' '

    def clean(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return ''.join(char for char in text if char != self.SPACE_CHAR)

if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_text1 = "  This is a sample text with spaces.  "
    cleaned_text1 = cleaner.clean(sample_text1)
    print(cleaned_text1)

    sample_text2 = "Another example with different spaces."
    cleaned_text2 = cleaner.clean(sample_text2)
    print(cleaned_text2)

    sample_text3 = "  Yet another test with spaces.  "
    cleaned_text3 = cleaner.clean(sample_text3)
    print(cleaned_text3)