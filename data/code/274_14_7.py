class ItemIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def has_next(self):
        return self.index < len(self.items)

    def next_item(self):
        if self.has_next():
            item = self.items[self.index]
            self.index += 1
            return item
        return None

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    iterator = ItemIterator(sample_items)
    while iterator.has_next():
        print(iterator.next_item())