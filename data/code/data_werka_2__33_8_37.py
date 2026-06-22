class StringCleaner:
    def clean(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        cleaned_text = []
        for char in text:
            if char != ' ':
                cleaned_text.append(char)
        return ''.join(cleaned_text)

if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_text = "Another example with different spaces."
    cleaned_text = cleaner.clean(sample_text)
    print(cleaned_text)