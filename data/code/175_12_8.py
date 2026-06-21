import re

class SentenceSeparator:
    def __init__(self):
        self.delimiters = r'[ ,.]+'

    def separate(self, sentence):
        return re.split(self.delimiters, sentence)

if __name__ == '__main__':
    separator = SentenceSeparator()
    sample_sentence = "Hello, world. This is a test."
    words = separator.separate(sample_sentence)
    print(words)