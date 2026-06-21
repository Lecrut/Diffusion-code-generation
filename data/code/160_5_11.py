from collections import Counter

class ItemManager:
    def __init__(self, item_list):
        self.item_counter = Counter(item_list)

    def get_item_count(self, item_name):
        return self.item_counter[item_name]

if __name__ == '__main__':
    manager = ItemManager(['apple', 'banana', 'apple', 'orange', 'banana', 'banana'])
    print(manager.get_item_count('apple'))
    print(manager.get_item_count('banana'))
    print(manager.get_item_count('orange'))