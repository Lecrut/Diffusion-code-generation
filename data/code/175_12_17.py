import re

class SentenceSplitter:
    def __init__(self):
        self.pattern = r'[ ,.]+'

    def split_sentence(self, sentence):
        return re.split(self.pattern, sentence)

if __name__ == '__main__':
    splitter = SentenceSplitter()
    sample_sentence = "Hello, world. This is a test."
    words = splitter.split_sentence(sample_sentence)
    print(words)