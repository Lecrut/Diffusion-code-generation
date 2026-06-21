from collections import Counter

class ItemCounter:
    def __init__(self, items):
        self.item_counts = Counter(items)

    def get_count(self, item):
        return self.item_counts.get(item, 0)

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    counter = ItemCounter(sample_items)
    print(counter.get_count('apple'))
    print(counter.get_count('banana'))
    print(counter.get_count('orange'))