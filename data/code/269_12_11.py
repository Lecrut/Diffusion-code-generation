import re

class PunctuationIsolator:
    def __init__(self):
        self.punctuation_patterns = [re.compile(r'[^\w\s]')]

    def isolate(self, sentences):
        return [self._isolate_sentence(sentence) for sentence in sentences]

    def _isolate_sentence(self, sentence):
        return self.punctuation_patterns[0].findall(sentence)

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