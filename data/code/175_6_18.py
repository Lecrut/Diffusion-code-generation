import re

def custom_word_splitter(sentence):
    delimiters = [' ', ',', '.', '!', '?']
    pattern = '|'.join(map(re.escape, delimiters))
    words = re.split(pattern, sentence)
    return [word for word in words if word]

if __name__ == '__main__':
    sample_sentence = "Hello, world! How are you doing today?"
    result = custom_word_splitter(sample_sentence)
    print(result)