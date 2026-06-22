import re

def isolate_punctuation(sentences):
    return [re.findall(r'[^\w\s]', sentence) for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello, world!",
        "Is it raining?",
        "This is a test sentence.",
        "No punctuation here."
    ]
    isolated_punctuation = isolate_punctuation(sample_sentences)
    print(isolated_punctuation)