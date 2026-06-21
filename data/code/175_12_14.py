import re

class SentenceSeparator:
    def __init__(self):
        self.pattern = r'[ ,.]+'

    def separate_words(self, sentence):
        words = re.split(self.pattern, sentence)
        return [word for word in words if word]

if __name__ == '__main__':
    separator = SentenceSeparator()
    sample_sentence = "Hello, world. This is a test."
    print(separator.separate_words(sample_sentence))