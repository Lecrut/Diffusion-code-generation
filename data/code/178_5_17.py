import re

class WordExtractor:
    _ALPHANUMERIC_PATTERN = re.compile(r'\W+')

    @staticmethod
    def extract_words(text):
        cleaned_text = WordExtractor._ALPHANUMERIC_PATTERN.sub(' ', text)
        words = cleaned_text.split()
        return [word.lower() for word in words if word]

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with some - punctuation and numbers 123."
    extractor = WordExtractor()
    result = extractor.extract_words(sample_string)
    print(result)