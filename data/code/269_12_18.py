import re

def isolate_punctuation(sentences):
    return [re.findall(r'[^\w\s]', sentence) for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello, world!",
        "Python is great.",
        "Let's meet at 3:00 p.m."
    ]
    print(isolate_punctuation(sample_sentences))