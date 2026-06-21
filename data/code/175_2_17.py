import re

class SentenceSeparator:
    DELIMITERS = r'[^\w\s]'
    
    @staticmethod
    def replace_delimiters(sentence):
        return re.sub(SentenceSeparator.DELIMITERS, ' ', sentence)
    
    @staticmethod
    def split_sentence(sentence):
        return [word.strip() for word in sentence.split()]
    
    @staticmethod
    def separate_words(sentence):
        cleaned_sentence = SentenceSeparator.replace_delimiters(sentence)
        words = SentenceSeparator.split_sentence(cleaned_sentence)
        return words

if __name__ == '__main__':
    sample_sentence = "Hello, world! This is a test... with multiple delimiters."
    separator = SentenceSeparator()
    print(separator.separate_words(sample_sentence))