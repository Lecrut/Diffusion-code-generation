import re

class WordSeparator:
    DELIMITERS = r'[^\w\s]'
    
    @staticmethod
    def separate_words(sentence):
        cleaned_sentence = re.sub(WordSeparator.DELIMITERS, ' ', sentence)
        words = [word.strip() for word in cleaned_sentence.split()]
        return words

if __name__ == '__main__':
    sample_sentence = "Hello, world! This is a test... with multiple delimiters."
    separator = WordSeparator()
    print(separator.separate_words(sample_sentence))