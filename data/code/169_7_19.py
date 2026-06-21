class ItemCounter:
    def __init__(self):
        self.counts = {}

    def update_count(self, item_name, quantity):
        if quantity <= 0:
            return
        if item_name in self.counts:
            self.counts[item_name] += quantity
        else:
            self.counts[item_name] = quantity

    def get_counts(self):
        return sorted((item, count) for item, count in self.counts.items())

if __name__ == '__main__':
    counter = ItemCounter()
    transactions = [('apple', 3), ('banana', -1), ('apple', 2), ('orange', 5)]
    for item, quantity in transactions:
        counter.update_count(item, quantity)
    print(counter.get_counts())