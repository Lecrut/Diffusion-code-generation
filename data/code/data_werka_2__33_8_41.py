class StringCleaner:
    def clean(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        result = []
        for char in text:
            if char != ' ':
                result.append(char)
        return ''.join(result)

if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_text = "A unique example with spaces to remove."
    cleaned_text = cleaner.clean(sample_text)
    print(cleaned_text)