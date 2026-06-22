class StringCleaner:
    def __init__(self):
        self.strip_characters = {' ': None}

    def clean(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        cleaned_text = []
        for char in text:
            if char not in self.strip_characters:
                cleaned_text.append(char)
        
        return ''.join(cleaned_text)

if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_text = "  This is a sample text with spaces.  "
    cleaned_text = cleaner.clean(sample_text)
    print(cleaned_text)