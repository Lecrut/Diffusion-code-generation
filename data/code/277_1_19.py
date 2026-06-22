class ItemCounter:
    def __init__(self):
        self.occurrences = {}

    def count(self, dictionary):
        for key, value in dictionary.items():
            if value not in self.occurrences:
                self.occurrences[value] = 0
            self.occurrences[value] += 1

    def get_counts(self):
        return self.occurrences

if __name__ == '__main__':
    counter = ItemCounter()
    sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
    counter.count(sample_dict)
    print(counter.get_counts())