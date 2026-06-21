from collections import Counter

class ItemCounter:
    def __init__(self, items):
        self.counter = Counter(items)

    def get_count(self, item_name):
        return self.counter[item_name]

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    counter_instance = ItemCounter(sample_items)
    print(counter_instance.get_count('apple'))
    print(counter_instance.get_count('banana'))
    print(counter_instance.get_count('orange'))