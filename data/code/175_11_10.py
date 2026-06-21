import re

class WordExtractor:
    CLEAN_PATTERN = re.compile(r'\W+')

    @staticmethod
    def clean_text(text):
        return WordExtractor.CLEAN_PATTERN.sub(' ', text)

    @staticmethod
    def extract_words(text):
        cleaned_text = WordExtractor.clean_text(text)
        return cleaned_text.split()

if __name__ == '__main__':
    extractor = WordExtractor()
    sample_text = "Hello, world! This is a test sentence. It contains punctuation and spaces."
    words = extractor.extract_words(sample_text)
    print(words)