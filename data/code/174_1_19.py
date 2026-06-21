class WordFrequencyCounter:
    def __init__(self):
        self.word_count = {}

    def count_words(self, words):
        for word in words:
            if word in self.word_count:
                self.word_count[word] += 1
            else:
                self.word_count[word] = 1

    def get_sorted_word_frequencies(self):
        return sorted(self.word_count.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    counter = WordFrequencyCounter()
    sample_words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    counter.count_words(sample_words)
    frequencies = counter.get_sorted_word_frequencies()
    print(frequencies)