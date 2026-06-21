import re

class WordExtractor:
    WORD_PATTERN = r'\b\w+\b'

    @staticmethod
    def extract_words(text):
        words = set()
        for word in re.findall(WordExtractor.WORD_PATTERN, text.lower()):
            words.add(word)
        return list(words)

if __name__ == '__main__':
    sample_string = "Hello world! This is a test, world, and hello again."
    extractor = WordExtractor()
    result = extractor.extract_words(sample_string)
    print(result)