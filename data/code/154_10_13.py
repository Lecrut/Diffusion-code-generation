from collections import Counter

class ElementCounter:
    def __init__(self, data_list):
        self.data = data_list
        self.counts = Counter(data_list)

    def get_counts(self):
        return self.counts

if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    counter_instance = ElementCounter(sample_list)
    print(f"Counts of elements: {counter_instance.get_counts()}")