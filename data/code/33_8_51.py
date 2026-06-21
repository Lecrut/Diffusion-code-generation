class StringCleaner:
    SPACE_CHAR = ' '
    
    @staticmethod
    def _remove_spaces(text):
        return ''.join(char for char in text if char != StringCleaner.SPACE_CHAR)
    
    def clean(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return StringCleaner._remove_spaces(text)

if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_text = "  This is a new sample text with spaces.  "
    cleaned_text = cleaner.clean(sample_text)
    print(cleaned_text)