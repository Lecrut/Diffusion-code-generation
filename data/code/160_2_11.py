class ItemCounter:
    def __init__(self):
        self.frequency_dict = {}

    @staticmethod
    def _increment_frequency(item, freq_dict):
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1

    def add_item(self, item_name):
        ItemCounter._increment_frequency(item_name, self.frequency_dict)

if __name__ == '__main__':
    counter = ItemCounter()
    counter.add_item("apple")
    counter.add_item("banana")
    counter.add_item("cherry")
    print(counter.frequency_dict)