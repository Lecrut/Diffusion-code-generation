import re

class SentenceSplitter:
    DELIMITERS = r'[ ,.]+'

    @staticmethod
    def separate_words(sentence):
        return re.split(SentenceSplitter.DELIMITERS, sentence)

if __name__ == '__main__':
    splitter = SentenceSplitter()
    sample_sentence = "Hello, world. This is a test."
    print(splitter.separate_words(sample_sentence))