from collections import Counter

class ItemCounter:
    def __init__(self, items):
        self.items = Counter(items)

    def get_count(self, item_name):
        return self.items[item_name]

    def most_common_item(self):
        return self.items.most_common(1)

if __name__ == '__main__':
    sample_items = {'apples': 3, 'bananas': 2, 'oranges': 5}
    counter = ItemCounter(sample_items)
    
    print(counter.get_count('apples'))
    print(counter.get_count('bananas'))
    print(counter.get_count('oranges'))
    print(counter.most_common_item())