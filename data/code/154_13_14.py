class FrequencyCounter:
    def __init__(self, items):
        self.items = items
        self.frequency_map = {item: items.count(item) for item in set(items)}

    def get_frequency(self, item):
        return self.frequency_map.get(item, 0)

if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    counter_instance = FrequencyCounter(sample_data)
    print(counter_instance.get_frequency('apple'))
    print(counter_instance.get_frequency('banana'))
    print(counter_instance.get_frequency('orange'))
    print(counter_instance.get_frequency('grape'))