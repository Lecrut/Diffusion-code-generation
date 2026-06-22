import re

class PunctuationCounter:
    def __init__(self):
        self.punctuation_count = {}

    def count_punctuation(self, text):
        punctuation_marks = r'[.,!?;:()[]{}]'
        found_punctuations = re.findall(punctuation_marks, text)
        for punct in found_punctuations:
            if punct in self.punctuation_count:
                self.punctuation_count[punct] += 1
            else:
                self.punctuation_count[punct] = 1

    def get_punctuation_counts(self):
        return self.punctuation_count

if __name__ == '__main__':
    text = "Hello, world! How are you?"
    counter = PunctuationCounter()
    counter.count_punctuation(text)
    print(counter.get_punctuation_counts())