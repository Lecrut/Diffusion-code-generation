import re

class WordExtractor:
    @staticmethod
    def extract_words(sentence):
        return re.findall(r'\b\w+\b', sentence)

if __name__ == '__main__':
    extractor = WordExtractor()
    sample_sentence = "This is a sample sentence for testing"
    words = extractor.extract_words(sample_sentence)
    print(words)