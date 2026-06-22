class TextProcessor:
    def clean_text(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return ''.join(text.split())

if __name__ == '__main__':
    processor = TextProcessor()
    sample_text = "  This is a   sample text with \n various   whitespaces.  "
    cleaned_text = processor.clean_text(sample_text)
    print(cleaned_text)