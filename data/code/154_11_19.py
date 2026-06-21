class ItemFrequencyCounter:
    def __init__(self):
        self.frequency = {}

    def add_item(self, item):
        if item in self.frequency:
            self.frequency[item] += 1
        else:
            self.frequency[item] = 1

    def get_frequency(self):
        return self.frequency

if __name__ == '__main__':
    counter = ItemFrequencyCounter()
    items = [1, 2, 3, 4, 5, 2, 3, 3]
    for item in items:
        counter.add_item(item)
    print(counter.get_frequency())