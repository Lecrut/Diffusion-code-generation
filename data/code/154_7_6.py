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
    for _ in range(5):
        counter.add_string('apple')
    counter.add_string('banana')
    result = counter.count_and_sort_strings()
    print(result)