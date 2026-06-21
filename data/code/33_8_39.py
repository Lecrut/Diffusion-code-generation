class StringCleaner:
    SPACE_CHAR = ' '

    @staticmethod
    def _is_string(text):
        return isinstance(text, str)

    def clean(self, text):
        if not self._is_string(text):
            raise ValueError("Input must be a string")
        return ''.join(char for char in text if char != self.SPACE_CHAR)

if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_text = "  This is a unique example with spaces.  "
    cleaned_text = cleaner.clean(sample_text)
    print(cleaned_text)