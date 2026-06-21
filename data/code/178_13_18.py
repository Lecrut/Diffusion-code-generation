import re

class WordExtractor:
    def __init__(self):
        self.pattern = r'\b\w+\b'

    def extract_words(self, phrase):
        return re.findall(self.pattern, phrase.lower())

if __name__ == '__main__':
    extractor = WordExtractor()
    sample_phrase = "This is a complex example phrase with various words and punctuation."
    words = extractor.extract_words(sample_phrase)
    print(words)