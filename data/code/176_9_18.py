import re

class WordExtractor:
    WORD_PATTERN = r'\b[a-zA-Z]+\b'

    @staticmethod
    def find_letter_sequences(text):
        return re.findall(WordExtractor.WORD_PATTERN, text)

if __name__ == '__main__':
    sample_text = "Hello, World! 123 Python 3.8"
    extractor = WordExtractor()
    result = extractor.find_letter_sequences(sample_text)
    print(result)