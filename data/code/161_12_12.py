class Item:
    def __init__(self, name, quantity):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")
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
            raise TypeError("Item must be an instance of Item class")
        self._items.append(item)

    def list_items(self):
        for item in self._items:
            print(str(item))

if __name__ == '__main__':
    try:
        my_list = ItemList()
        my_list.add_item(Item("Apple", 10))
        my_list.add_item(Item("Banana", 5))
        my_list.list_items()
    except (ValueError, TypeError) as e:
        print(e)