import re

class TextProcessor:
    def __init__(self, text):
        self.text = text.lower()

    def find_words(self):
        return re.findall(r'\b[a-z]+\b', self.text)

if __name__ == '__main__':
    processor = TextProcessor("Hello World! This is a test string, with numbers 123 and symbols @#$.")
    words = processor.find_words()
    print(words)