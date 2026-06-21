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
    updates = {'apple': 5, 'banana': 3}
    counter.add_items(updates)
    print(counter.unique_item_count())