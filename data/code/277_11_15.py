class ItemCounter:
    def __init__(self):
        self.counts = {}

    def count(self, data):
        for item in data:
            if item in self.counts:
                self.counts[item] += 1
            else:
                self.counts[item] = 1

    def get_counts(self):
        return self.counts

if __name__ == '__main__':
    counter = ItemCounter()
    sample_dict = {'apple': 2, 'banana': 5, 'cherry': 3}
    counter.count(sample_dict)
    print(counter.get_counts())

    sample_dict_empty = {}
    counter.count(sample_dict_empty)
    print(counter.get_counts())

    sample_dict_with_duplicates = {'apple': 1, 'banana': 1, 'apple': 2}
    counter.count(sample_dict_with_duplicates)
    print(counter.get_counts())