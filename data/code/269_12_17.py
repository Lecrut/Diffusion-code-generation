import re

def isolate_punctuation(sentences):
    punctuation_dict = {
        'punctuation': '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    }
    return [[char for char in sentence if char in punctuation_dict['punctuation']] for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello, world!",
        "Python is fun.",
        "Is it raining?",
        "No punctuation here"
    ]
    print(isolate_punctuation(sample_sentences))