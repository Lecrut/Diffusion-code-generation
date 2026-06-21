from collections import Counter

class StringFrequencyCounter:
    def __init__(self):
        self.frequency_dict = {}

    def count_strings(self, strings):
        counter = Counter(strings)
        sorted_counter = dict(counter.most_common())
        return sorted_counter

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    counter_instance = StringFrequencyCounter()
    result = counter_instance.count_strings(sample_strings)
    print(result)