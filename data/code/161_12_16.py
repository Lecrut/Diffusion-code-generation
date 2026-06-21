class Item:
    DEFAULT_QUANTITY = 1

    def __init__(self, name, quantity=DEFAULT_QUANTITY):
        self._name = name
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    def display_item(self):
        print(f"{self._name}: {self._quantity}")

class ItemList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_items(self):
        for item in self.items:
            item.display_item()

if __name__ == '__main__':
    sample_data = [
        ("Apple", 3),
        ("Banana", 5),
        ("Cherry", 2)
    ]
    my_list = ItemList()
    for name, quantity in sample_data:
        my_list.add_item(Item(name, quantity))
    my_list.list_items()