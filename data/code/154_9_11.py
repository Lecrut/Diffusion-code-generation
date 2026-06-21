class FrequencyCounter:
    def __init__(self):
        self.freqs = {}

    def add_items(self, items):
        if not hasattr(items, '__iter__'):
            raise TypeError("Input must be iterable")
        for item in items:
            if item in self.freqs:
                self.freqs[item] += 1
            else:
                self.freqs[item] = 1

    def get_frequencies(self):
        return self.freqs.copy()

if __name__ == '__main__':
    counter = FrequencyCounter()
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    counter.add_items(sample_items)
    print(counter.get_frequencies())