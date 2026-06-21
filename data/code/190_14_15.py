class ItemContainer:
    def __init__(self, items):
        self.items_set = set(items)

    def contains_item(self, value):
        return value in self.items_set

if __name__ == '__main__':
    container = ItemContainer([10, 20, 30, 40, 50])
    print(container.contains_item(30))
    print(container.contains_item(60))