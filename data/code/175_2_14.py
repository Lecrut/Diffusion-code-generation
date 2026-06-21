import re

def separate_words(sentence):
    DELIMITER = r'[^\w\s]'
    CLEANED_sentence = re.sub(DELIMITER, ' ', sentence)
    WORDS = CLEANED_sentence.split()
    return WORDS

if __name__ == '__main__':
    sample_sentence = "Hello, world! This is a test... with multiple delimiters."
    print(separate_words(sample_sentence))