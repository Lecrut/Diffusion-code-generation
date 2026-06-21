import re

def validate_input(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")

def separate_words(sentence):
    validate_input(sentence)
    cleaned_sentence = re.sub(r'[^\w\s]', ' ', sentence)
    words = [word.strip() for word in cleaned_sentence.split()]
    return words

if __name__ == '__main__':
    sample_sentence = "Hello, world! This is a test... with multiple delimiters."
    print(separate_words(sample_sentence))