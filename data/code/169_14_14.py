class ItemCounter:

    def __init__(self):
        self.counts = {}

    def add_counts(self, updates):
        for item, count in updates.items():
            if item in self.counts:
                self.counts[item] += count
            else:
                self.counts[item] = count

    def get_unique_items_count(self):
        return len(self.counts)
if __name__ == '__main__':
    counter = ItemCounter()
    counter.add_counts({'apple': 3, 'banana': 2})
    print(counter.get_unique_items_count())
    counter.add_counts({'banana': 1, 'orange': 5})
    print(counter.get_unique_items_count())