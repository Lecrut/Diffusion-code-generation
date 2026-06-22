class TextProcessor:
    def clean_text(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        return self._remove_whitespace(text)
    
    def _remove_whitespace(self, text):
        return ''.join(text.split())

if __name__ == '__main__':
    processor = TextProcessor()
    sample_text = "  This is   a sample \n text with various   whitespaces.  "
    cleaned_text = processor.clean_text(sample_text)
    print(cleaned_text)