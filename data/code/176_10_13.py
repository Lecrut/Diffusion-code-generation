import re

class WordExtractor:
    def __init__(self):
        self.pattern = r'\b\w+\b'

    def extract_words(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return re.findall(self.pattern, text)

if __name__ == '__main__':
    extractor = WordExtractor()
    sample_text1 = "This is a test string with words, including multiple sentences!"
    print(extractor.extract_words(sample_text1))
    
    sample_text2 = "Hello, this is another test string."
    print(extractor.extract_words(sample_text2))