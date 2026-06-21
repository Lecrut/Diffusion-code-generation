class WordFrequencyCounter:
    def __init__(self):
        self.frequency = {}

    def add_words(self, words):
        for word in words:
            if word in self.frequency:
                self.frequency[word] += 1
            else:
                self.frequency[word] = 1

    def get_sorted_frequency(self):
        return sorted(self.frequency.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    counter = WordFrequencyCounter()
    sample_words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    counter.add_words(sample_words)
    print(counter.get_sorted_frequency())