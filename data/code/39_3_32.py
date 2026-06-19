import re

class WordExtractor:
    WORD_PATTERN = r'\b\w+\b'

    @staticmethod
    def extract_words(input_string):
        words = re.findall(WordExtractor.WORD_PATTERN, input_string)
        return words

if __name__ == '__main__':
    sample_input = """Hello, world! This is a test string with multiple words,
    including numbers like 123 and special characters #@$%^&*()."""
    extractor = WordExtractor()
    extracted_words = extractor.extract_words(sample_input)
    print(extracted_words)