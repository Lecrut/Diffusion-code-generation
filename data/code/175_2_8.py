import re

class SentenceSeparator:
    def __init__(self):
        self.pattern = r'[^\w\s]+'

    def separate(self, sentence):
        cleaned_sentence = re.sub(self.pattern, ' ', sentence)
        words = [word.strip() for word in cleaned_sentence.split()]
        return words

if __name__ == '__main__':
    separator = SentenceSeparator()
    sample_sentence = "Hello, world! This is a test... with multiple delimiters."
    print(separator.separate(sample_sentence))