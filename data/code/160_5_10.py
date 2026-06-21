from collections import Counter

class ItemCounter:

    def __init__(self, items):
        self.item_counts = Counter(items)

    def get_count(self, item_name):
        return self.item_counts.get(item_name, 0)
if __name__ == '__main__':
    items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    counter = ItemCounter(items)
    print(counter.get_count('apple'))
    print(counter.get_count('banana'))
    print(counter.get_count('orange'))
    print(counter.get_count('grape'))