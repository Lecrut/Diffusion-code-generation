import re

class TextProcessor:
    def extract_words(self, text):
        return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    processor = TextProcessor()
    sample_text = "Hello world! This is a test."
    extracted_words = processor.extract_words(sample_text)
    print(extracted_words)