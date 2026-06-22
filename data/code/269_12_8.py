import re

def is_punctuation(char):
    return char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def isolate_punctuation(sentences):
    if not all(isinstance(sentence, str) for sentence in sentences):
        raise ValueError("All elements in the input list must be strings.")
    
    return [[char for char in sentence if is_punctuation(char)] for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello, world!",
        "Python is fun.",
        "Is it raining?",
        "No punctuation here"
    ]
    print(isolate_punctuation(sample_sentences))