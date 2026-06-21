class FrequencyCounter:

    def __init__(self):
        self.counts = {}

    def add_item(self, item):
        self.counts[item] = self.counts.get(item, 0) + 1

    def get_frequency(self, item):
        return self.counts.get(item, 0)
if __name__ == '__main__':
    counter = FrequencyCounter()
    data_list = [1, 2, 3, 2, 4, 2, 5, 2]
    for item in data_list:
        counter.add_item(item)
    print(counter.get_frequency(2))
    print(counter.get_frequency(1))
    print(counter.get_frequency(3))
    print(counter.get_frequency(4))
    print(counter.get_frequency(5))
    print(counter.get_frequency(6))