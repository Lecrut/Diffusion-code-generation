import re

def isolate_punctuation(sentences):
    return [re.findall(r'[^\w\s]', sentence) for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello, world!",
        "This is a test.",
        "Python programming: fun and challenging!"
    ]
    print(isolate_punctuation(sample_sentences))