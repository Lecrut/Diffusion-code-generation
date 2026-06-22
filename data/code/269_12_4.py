import re

def isolate_punctuation(sentences):
    return [re.findall(r'[^\w\s]', sentence) for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello, world! How are you?",
        "Python's syntax is quite interesting.",
        "Is it raining? Yes, it is."
    ]
    print(isolate_punctuation(sample_sentences))