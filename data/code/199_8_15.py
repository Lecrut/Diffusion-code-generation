from collections import Counter

class NameFrequencyCounter:
    def __init__(self, names):
        self.names = names
        self.frequency_counter = Counter(names)

    def get_frequency_list(self):
        return sorted(self.frequency_counter.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Bob']
    counter_instance = NameFrequencyCounter(sample_names)
    frequency_list = counter_instance.get_frequency_list()
    print(frequency_list)