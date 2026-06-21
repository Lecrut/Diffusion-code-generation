class FrequencyCounter:
    def __init__(self):
        self.frequency = {}

    def add_item(self, item):
        if item in self.frequency:
            self.frequency[item] += 1
        else:
            self.frequency[item] = 1

    def get_frequency(self, item):
        return self.frequency.get(item, 0)

if __name__ == '__main__':
    counter = FrequencyCounter()
    items = [1, 2, 3, 4, 5, 2, 3, 1]
    for item in items:
        counter.add_item(item)
    
    print(f"Frequency of 1: {counter.get_frequency(1)}")
    print(f"Frequency of 2: {counter.get_frequency(2)}")
    print(f"Frequency of 3: {counter.get_frequency(3)}")
    print(f"Frequency of 4: {counter.get_frequency(4)}")
    print(f"Frequency of 5: {counter.get_frequency(5)}")
    print(f"Frequency of 6: {counter.get_frequency(6)}")