from collections import Counter

class NameFrequencyCounter:
    def __init__(self, names):
        self.names = names
        self.frequency_counter = Counter(names)

    def get_frequency_sorted(self):
        return sorted(self.frequency_counter.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    name_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Alice"]
    counter_instance = NameFrequencyCounter(name_list)
    result = counter_instance.get_frequency_sorted()
    print(result)