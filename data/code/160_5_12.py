from collections import Counter

class ItemManager:
    def __init__(self, items):
        self.item_counter = Counter(items)

    def get_count(self, item_name):
        return self.item_counter.get(item_name, 0)

if __name__ == '__main__':
    manager = ItemManager(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
    print(manager.get_count('apple'))
    print(manager.get_count('banana'))
    print(manager.get_count('cherry'))