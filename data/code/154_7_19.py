from collections import Counter

class StringCounter:
    def __init__(self):
        self.strings = []

    def add_string(self, string):
        self.strings.append(string)

    def count_and_sort_strings(self):
        return dict(Counter(self.strings).most_common())

if __name__ == '__main__':
    counter = StringCounter()
    sample_strings = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    for string in sample_strings:
        counter.add_string(string)
    result = counter.count_and_sort_strings()
    print(result)