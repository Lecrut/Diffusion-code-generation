class ItemCounter:
    def __init__(self):
        self.items = {}

    def update(self, updates):
        for item, count in updates.items():
            if item in self.items:
                self.items[item] += count
            else:
                self.items[item] = count

    def unique_items_count(self):
        return len(self.items)

if __name__ == '__main__':
    counter = ItemCounter()
    counter.update({'apple': 3, 'banana': 2})
    counter.update({'orange': 1, 'apple': 1})
    print(counter.unique_items_count())