class ItemCounter:
    def __init__(self):
        self.items = {}

    def add_counts(self, updates):
        for item, count in updates.items():
            if item in self.items:
                self.items[item] += count
            else:
                self.items[item] = count

    def get_unique_count(self):
        return len(self.items)

if __name__ == '__main__':
    counter = ItemCounter()
    counter.add_counts({'apple': 3, 'banana': 2})
    print(counter.get_unique_count())