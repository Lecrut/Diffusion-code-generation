import re

class WordExtractor:
    _pattern = re.compile(r'\b\w+\b')

    @staticmethod
    def extract_words(text):
        return [word.lower() for word in WordExtractor._pattern.findall(text)]

if __name__ == '__main__':
    sample_string = "Hello world! This is a test, how are you doing today? Python programming is fun."
    extracted_words = WordExtractor.extract_words(sample_string)
    print(extracted_words)