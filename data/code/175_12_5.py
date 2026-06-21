import re

class WordSeparator:
    DELIMITERS = r'[ ,.]+'

    @staticmethod
    def separate_words(sentence):
        return re.split(WordSeparator.DELIMITERS, sentence)

if __name__ == '__main__':
    sample_sentence = "Hello, world. This is a test."
    words = WordSeparator.separate_words(sample_sentence)
    print(words)