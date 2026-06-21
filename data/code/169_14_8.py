class ItemCounter:

    def __init__(self):
        self.counts = {}

    def add_items(self, updates):
        for item, count in updates.items():
            if item in self.counts:
                self.counts[item] += count
            else:
                self.counts[item] = count

    def unique_item_count(self):
        return len(self.counts)
if __name__ == '__main__':
    counter = ItemCounter()
    counter.add_items({'apple': 3, 'banana': 2})
    print(counter.unique_item_count())
    counter.add_items({'banana': 1, 'orange': 5})
    print(counter.unique_item_count())