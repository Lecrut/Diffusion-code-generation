class Item:
    def __init__(self, name, quantity):
        self._name = name
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    def __str__(self):
        return f"{self._name}: {self._quantity}"

class ItemList:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def list_items(self):
        for item in self._items:
            print(item)

if __name__ == '__main__':
    sample_data = [
        ("Apple", 10),
        ("Banana", 20),
        ("Cherry", 30)
    ]
    
    my_list = ItemList()
    for name, quantity in sample_data:
        item = Item(name, quantity)
        my_list.add_item(item)
    
    my_list.list_items()