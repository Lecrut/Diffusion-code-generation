import re

class WordExtractor:
    @staticmethod
    def extract_words(text):
        return re.findall(r'\b\w+\b', text.lower())

if __name__ == '__main__':
    extractor = WordExtractor()
    sample_string = "Hello world! This is a test, how are you doing today? Python programming is fun."
    extracted_words = extractor.extract_words(sample_string)
    print(extracted_words)