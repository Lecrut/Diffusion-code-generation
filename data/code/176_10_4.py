import re

class WordExtractor:
    def extract_words(self, text):
        return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    extractor = WordExtractor()
    sample_text = "Hello, this is a test string with words."
    words = extractor.extract_words(sample_text)
    print(words)