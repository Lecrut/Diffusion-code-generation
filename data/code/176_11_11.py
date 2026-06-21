import re

class WordExtractor:
    WORD_PATTERN = r'\b\w+\b'
    
    @staticmethod
    def find_words(text):
        return re.findall(WordExtractor.WORD_PATTERN, text)

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. Multiple   spaces and punctuation... should work."
    words = WordExtractor.find_words(sample_text)
    print(words)