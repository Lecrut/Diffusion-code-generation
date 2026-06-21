class ItemCounter:
    def __init__(self, counts=None):
        self.counts = {} if counts is None else counts

    def add_counts(self, other):
        for key, value in other.items():
            self.counts[key] = (self.counts.get(key, 0) + value)

    def subtract_counts(self, other):
        for key, value in other.items():
            self.counts[key] = (self.counts.get(key, 0) - value)
        self.counts = {k: v for k, v in self.counts.items() if v != 0}

def compare_item_counts(dict1=None, dict2=None):
    counter1 = ItemCounter(dict1)
    counter2 = ItemCounter(dict2)
    counter1.subtract_counts(counter2.counts)
    return counter1.counts

if __name__ == '__main__':
    sample_dict1 = {'apple': 3, 'banana': 5, 'cherry': 2}
    sample_dict2 = {'banana': 2, 'cherry': 4, 'date': 7}
    print(compare_item_counts(sample_dict1, sample_dict2))