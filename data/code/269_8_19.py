import re

class PunctuationCounter:
    def __init__(self):
        self.punctuation_counts = {}

    def count_punctuation(self, text):
        punctuation_marks = re.findall(r'[.,!?;:()[]{}]', text)
        for mark in punctuation_marks:
            if mark in self.punctuation_counts:
                self.punctuation_counts[mark] += 1
            else:
                self.punctuation_counts[mark] = 1

    def get_punctuation_counts(self):
        return self.punctuation_counts

if __name__ == '__main__':
    counter = PunctuationCounter()
    text = "Hello, world! How are you? I am fine."
    counter.count_punctuation(text)
    print(counter.get_punctuation_counts())