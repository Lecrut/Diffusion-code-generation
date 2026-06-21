import re

class WordExtractor:
    @staticmethod
    def extract_words(phrase):
        return re.findall(r'\b\w+\b', phrase.lower())

if __name__ == '__main__':
    extractor = WordExtractor()
    sample_phrase = "This is a complex example phrase with various words and punctuation!"
    words = extractor.extract_words(sample_phrase)
    print(words)