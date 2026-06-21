class FrequencyCounter:
    def __init__(self):
        self.freqs = {}

    def update(self, item):
        self.freqs[item] = self.freqs.get(item, 0) + 1

    def get_frequency(self, item):
        return self.freqs.get(item, 0)

if __name__ == '__main__':
    counter = FrequencyCounter()
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    for item in sample_list:
        counter.update(item)
    print(counter.get_frequency('apple'))
    print(counter.get_frequency('banana'))
    print(counter.get_frequency('orange'))