class ItemCounter:
    def __init__(self):
        self.counts = {}

    def add_item(self, item):
        if not isinstance(item, list):
            key = item
        else:
            key = tuple(sorted(item))
        if key in self.counts:
            self.counts[key] += 1
        else:
            self.counts[key] = 1

    def get_counts(self):
        return self.counts

if __name__ == '__main__':
    counter = ItemCounter()
    items = [1, "a", 3.14, True, [1, 2], [], ["hello"], None]
    for item in items:
        counter.add_item(item)
    print(counter.get_counts())