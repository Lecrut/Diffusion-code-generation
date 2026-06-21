import re

def separate_words(sentence):
    cleaned_sentence = re.sub(r'[^\w\s]', ' ', sentence)
    words = [word.strip() for word in cleaned_sentence.split()]
    return words

if __name__ == '__main__':
    sample_sentence = "Hello, world! This is a test... with multiple delimiters."
    result = separate_words(sample_sentence)
    print(result)