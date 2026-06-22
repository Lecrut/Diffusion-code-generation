class TextProcessor:
    def clean_text(self, text):
        return ''.join(text.split())

if __name__ == '__main__':
    processor = TextProcessor()
    sample_text = "  Hello   World! This is a\ttest.  "
    cleaned_text = processor.clean_text(sample_text)
    print(cleaned_text)