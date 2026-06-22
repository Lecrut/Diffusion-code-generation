import collections

class WordCounter:
    def __init__(self, text):
        self.text = text
        self.word_counts = None

    def count_words(self):
        if not self.text:
            return {}
        words = self.text.split()
        self.word_counts = collections.Counter(words)
        return self.word_counts

    def get_top_n_words(self, n=10):
        if self.word_counts is None:
            self.count_words()
        top_n = self.word_counts.most_common(n)
        return top_n

if __name__ == '__main__':
    sample_text = "This is an example sentence for word counting. This sentence contains some repeated words."
    counter = WordCounter(sample_text)
    print(counter.get_top_n_words(5))