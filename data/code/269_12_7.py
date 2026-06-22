import re

class PunctuationIsolator:
    def isolate(self, sentences):
        return [re.findall(r'[^\w\s]', sentence) for sentence in sentences]

if __name__ == '__main__':
    isolator = PunctuationIsolator()
    sample_sentences = [
        "Hello, world!",
        "Python is fun.",
        "Is it raining?",
        "No punctuation here"
    ]
    results = isolator.isolate(sample_sentences)
    print(results)