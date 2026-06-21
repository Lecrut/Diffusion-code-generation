from collections import Counter

class ItemCounter:
    def __init__(self):
        self.counts = Counter()

    def add_item(self, item, count=1):
        self.counts[item] += count

    def get_counts(self):
        return dict(self.counts)

if __name__ == '__main__':
    counter = ItemCounter()
    items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    for item in items:
        counter.add_item(item)
    
    print(counter.get_counts())