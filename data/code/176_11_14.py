import re

class WordFinder:
    def __init__(self):
        self.pattern = r'\b\w+\b'

    def find_words(self, text):
        return re.findall(self.pattern, text)

if __name__ == '__main__':
    finder = WordFinder()
    sample_text = "Hello, world! This is a test. Multiple   spaces and punctuation... should work."
    words = finder.find_words(sample_text)
    print(words)