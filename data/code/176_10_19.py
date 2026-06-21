import re

class WordExtractor:
    def __init__(self):
        self.pattern = r'\b\w+\b'

    def extract_words(self, text):
        return re.findall(self.pattern, text)

if __name__ == '__main__':
    extractor = WordExtractor()
    sample_text = "This is a test string with words, including multiple sentences!"
    words = extractor.extract_words(sample_text)
    print(words)