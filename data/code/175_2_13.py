import re

class SentenceProcessor:
    DELIMITERS = r'[^\w\s]'

    @staticmethod
    def replace_delimiters(sentence):
        return re.sub(SentenceProcessor.DELIMITERS, ' ', sentence)

    @staticmethod
    def split_sentence(sentence):
        words = sentence.split()
        return [word.strip() for word in words]

def separate_words(sentence):
    cleaned_sentence = SentenceProcessor.replace_delimiters(sentence)
    return SentenceProcessor.split_sentence(cleaned_sentence)

if __name__ == '__main__':
    sample_sentence = "Hello, world! This is a test... with multiple delimiters."
    print(separate_words(sample_sentence))