class ItemCounter:
    def __init__(self):
        self.counts = {}

    def add_item(self, item):
        if item in self.counts:
            self.counts[item] += 1
        else:
            self.counts[item] = 1

    def get_counts(self):
        return self.counts

if __name__ == '__main__':
    counter = ItemCounter()
    items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    for item in items:
        counter.add_item(item)
    print(counter.get_counts())