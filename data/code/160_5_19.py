from collections import Counter

class ItemManager:
    def __init__(self, initial_items=None):
        self.items = Counter(initial_items) if initial_items else Counter()

    def add_item(self, item, count=1):
        self.items[item] += count

    def get_count(self, item):
        return self.items.get(item, 0)

    def update_counts(self, updates):
        self.items.update(updates)

if __name__ == '__main__':
    manager = ItemManager(apples=3, bananas=2, oranges=5)
    print("Initial counts:", manager.items)
    manager.add_item('apples', 1)
    print("After adding apples:", manager.items)
    print("Count of bananas:", manager.get_count('bananas'))
    manager.update_counts({'oranges': 2})
    print("After updating oranges:", manager.items)