class ItemCounter:

    def __init__(self):
        self.counts = {}

    def update(self, items):
        for item, count in items.items():
            if item in self.counts:
                self.counts[item] += count
            else:
                self.counts[item] = count

    def unique_items_count(self):
        return len(self.counts)
if __name__ == '__main__':
    counter = ItemCounter()
    counter.update({'apple': 3, 'banana': 2})
    print(counter.unique_items_count())
    counter.update({'banana': 1, 'orange': 5})
    print(counter.unique_items_count())