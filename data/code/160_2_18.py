class ItemCounter:

    def __init__(self):
        self.item_counts = {}

    def add_item(self, item_name):
        if item_name in self.item_counts:
            self.item_counts[item_name] += 1
        else:
            self.item_counts[item_name] = 1

    def get_frequency(self, item_name):
        return self.item_counts.get(item_name, 0)
if __name__ == '__main__':
    counter = ItemCounter()
    items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    for item in items:
        counter.add_item(item)
    print(counter.get_frequency('apple'))
    print(counter.get_frequency('banana'))
    print(counter.get_frequency('cherry'))