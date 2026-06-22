class TextProcessor:
    def clean_text(self, text):
        words = text.split()
        cleaned_text = ''.join(words)
        return cleaned_text

if __name__ == '__main__':
    processor = TextProcessor()
    sample_text = "  Here is another   example with \t different types of whitespace.  "
    intermediate_result = processor.clean_text(sample_text)
    print(intermediate_result)