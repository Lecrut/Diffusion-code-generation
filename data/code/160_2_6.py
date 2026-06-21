class ItemFrequencyCounter:
    def __init__(self):
        self.frequency_dict = {}

    def add_item(self, item_name):
        if item_name in self.frequency_dict:
            self.frequency_dict[item_name] += 1
        else:
            self.frequency_dict[item_name] = 1

    def get_frequency(self, item_name):
        return self.frequency_dict.get(item_name, 0)

if __name__ == '__main__':
    counter = ItemFrequencyCounter()
    counter.add_item("apple")
    counter.add_item("banana")
    counter.add_item("apple")
    print(counter.get_frequency("apple"))
    print(counter.get_frequency("banana"))
    print(counter.get_frequency("cherry"))