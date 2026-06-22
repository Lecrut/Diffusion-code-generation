import re

PUNCTUATION_CHARS = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def isolate_punctuation(sentences):
    return [re.findall(f'[{PUNCTUATION_CHARS}]', sentence) for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello, world!",
        "Python is fun.",
        "Is it raining?",
        "No punctuation here"
    ]
    results = isolate_punctuation(sample_sentences)
    print(results)