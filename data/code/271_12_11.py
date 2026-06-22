from collections import Counter
import re

class WordCounter:
    def __init__(self):
        self.word_counts = Counter()

    def count_words(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        self.word_counts.update(words)

    def get_top_n_words(self, n):
        return self.word_counts.most_common(n)

if __name__ == '__main__':
    sample_text = "Hello world. Hello everyone. Welcome to the world of Python."
    counter = WordCounter()
    counter.count_words(sample_text)
    top_3_words = counter.get_top_n_words(3)
    print(top_3_words)