class FrequencyCounter:
    def __init__(self):
        self.freqs = {}

    def update(self, item):
        if item in self.freqs:
            self.freqs[item] += 1
        else:
            self.freqs[item] = 1

    def get_frequencies(self):
        return self.freqs

if __name__ == '__main__':
    counter = FrequencyCounter()
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    for item in sample_items:
        counter.update(item)
    print(counter.get_frequencies())