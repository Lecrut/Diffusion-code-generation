import re

def isolate_punctuation(text):
    punctuation_dict = {char: f' {char} ' for char in string.punctuation}
    return ''.join(punctuation_dict.get(char, char) for char in text)

if __name__ == '__main__':
    sample_text = "Hello, world! How are you?"
    print(isolate_punctuation(sample_text))