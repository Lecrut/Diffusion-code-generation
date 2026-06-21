import re

def separate_words(sentence):
    words = re.split(r'[ ,.]+', sentence)
    return [word for word in words if word]

if __name__ == '__main__':
    sample_sentence = "Hello, world! This is a test."
    result = separate_words(sample_sentence)
    print(result)