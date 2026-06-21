import re

class TextProcessor:
    @staticmethod
    def extract_words(text):
        words = re.findall(r'\b\w+\b', text.lower())
        return words

if __name__ == '__main__':
    processor = TextProcessor()
    sample_string = "Hello world! This is a test, how are you doing today? Python programming is fun."
    extracted_words = processor.extract_words(sample_string)
    print(extracted_words)