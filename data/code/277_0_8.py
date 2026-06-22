class ItemCounter:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def count_items(self):
        return len(self.items)

if __name__ == '__main__':
    counter = ItemCounter()
    for _ in range(5):
        counter.add_item(_)
    print(f"The number of items is: {counter.count_items()}")