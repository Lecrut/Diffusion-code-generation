from collections import Counter

class ItemManager:
    def __init__(self, items):
        self.items = Counter(items)

    def get_count(self, item_name):
        return self.items[item_name]

    def most_common_item(self):
        return self.items.most_common(1)

if __name__ == '__main__':
    manager = ItemManager(apples=3, bananas=2, oranges=5)
    print(manager.get_count('apples'))
    print(manager.get_count('bananas'))
    print(manager.get_count('oranges'))
    print(manager.most_common_item())