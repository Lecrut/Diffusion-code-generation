from collections import Counter
import re

class WordCounter:
    def __init__(self, text):
        self.text = text.lower()
        self.words = re.findall(r'\b\w+\b', self.text)
        self.word_counts = Counter(self.words)

    def get_top_n_words(self, n):
        return self.word_counts.most_common(n)

if __name__ == '__main__':
    sample_text = "Hello world. Hello everyone! Welcome to the world of Python."
    counter = WordCounter(sample_text)
    top_3_words = counter.get_top_n_words(3)
    print(top_3_words)