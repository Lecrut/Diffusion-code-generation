class Item:
    def __init__(self, name, quantity):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Item quantity must be a non-negative integer")
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
        if not isinstance(item, Item):
            raise ValueError("Invalid item type. Expected an instance of Item")
        self._items.append(item)

    def list_items(self):
        for item in self._items:
            print(item)

if __name__ == '__main__':
    try:
        sample_data = [
            Item("Apple", 3),
            Item("Banana", 5),
            Item("Cherry", 10)
        ]
        my_list = ItemList()
        for item in sample_data:
            my_list.add_item(item)
        my_list.list_items()
    except ValueError as e:
        print(e)