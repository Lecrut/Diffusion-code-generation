from collections import Counter

class ItemCounter:
    def __init__(self, items):
        self.counter = Counter(items)
    
    def get_count(self, item):
        return self.counter[item]

if __name__ == '__main__':
    items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    counter_instance = ItemCounter(items)
    print(counter_instance.get_count('apple'))
    print(counter_instance.get_count('banana'))
    print(counter_instance.get_count('orange'))