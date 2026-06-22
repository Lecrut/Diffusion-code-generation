class TextProcessor:
    def clean_text(self, text):
        return ''.join(text.split())

if __name__ == '__main__':
    processor = TextProcessor()
    sample_text = "  This is   a sample \n text with various   whitespaces.  "
    cleaned_text = processor.clean_text(sample_text)
    print(cleaned_text)