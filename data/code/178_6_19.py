import re

class WordExtractor:
    def __init__(self):
        self.pattern = r'\b\w{2,}\b'

    def extract_words(self, sentence):
        return re.findall(self.pattern, sentence)

if __name__ == '__main__':
    extractor = WordExtractor()
    sample_sentence = "This is a test sentence with some words."
    extracted_words = extractor.extract_words(sample_sentence)
    print(extracted_words)