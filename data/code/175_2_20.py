import re

class WordSeparator:
    def __init__(self):
        self.pattern = r'[^\w\s]'

    def clean_sentence(self, sentence):
        return re.sub(self.pattern, ' ', sentence)

    def split_sentence(self, cleaned_sentence):
        return [word.strip() for word in cleaned_sentence.split()]

    def separate_words(self, sentence):
        cleaned = self.clean_sentence(sentence)
        return self.split_sentence(cleaned)

if __name__ == '__main__':
    separator = WordSeparator()
    sample_sentence = "Hello, world! This is a test... with multiple delimiters."
    words = separator.separate_words(sample_sentence)
    print(words)