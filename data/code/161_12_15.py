class Item:
    def __init__(self, name: str, quantity: int):
        self._name = name
        self._quantity = quantity

    @property
    def name(self) -> str:
        return self._name

    @property
    def quantity(self) -> int:
        return self._quantity

    def __str__(self) -> str:
        return f"{self._name}: {self._quantity}"

class ItemList:
    def __init__(self):
        self._items = []

    def add_item(self, item: Item):
        self._items.append(item)

    def display_items(self):
        for item in self._items:
            print(item)

if __name__ == '__main__':
    sample_data = [
        Item("Apple", 10),
        Item("Banana", 5),
        Item("Cherry", 20)
    ]
    my_list = ItemList()
    for item in sample_data:
        my_list.add_item(item)
    my_list.display_items()