from typing import Generic, TypeVar

T = TypeVar('T')

class Item(Generic[T]):
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"

class Inventory(Generic[T]):
    def __init__(self):
        self.items = {}

    def add_item(self, item: Item[T]) -> None:
        if not isinstance(item, Item):
            raise TypeError("Item must be an instance of Item")
        if item.name in self.items:
            self.items[item.name].quantity += item.quantity
        else:
            self.items[item.name] = item

    def get_item(self, name: str) -> Item[T]:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        return self.items.get(name)

if __name__ == '__main__':
    inventory = Inventory()
    item1 = Item('apple', 5)
    inventory.add_item(item1)
    print(inventory.get_item('apple'))