from collections import Counter

class ItemCounter:
    def __init__(self, items):
        self.counter = Counter(items)

    def get_count(self, item_name):
        return self.counter.get(item_name, 0)

    def most_common(self, n=None):
        return self.counter.most_common(n)

if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", "date", "apple"]
    counter_instance = ItemCounter(sample_items)
    
    print(counter_instance.get_count("apple"))
    print(counter_instance.get_count("banana"))
    print(counter_instance.most_common())
    print(counter_instance.most_common(1))