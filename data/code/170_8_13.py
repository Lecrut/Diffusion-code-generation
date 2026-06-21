from typing import TypeVar, Generic, Dict

T = TypeVar('T')

class Item(Generic[T]):
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

class Inventory(Generic[T]):
    def __init__(self):
        self.items: Dict[str, T] = {}

    def add_item(self, item: T) -> None:
        if not isinstance(item, Item):
            raise TypeError("Item must be an instance of Item")
        if item.name in self.items:
            self.items[item.name].quantity += item.quantity
        else:
            self.items[item.name] = item

    def get_quantity(self, name: str) -> int:
        return self.items.get(name, Item("", 0)).quantity

if __name__ == '__main__':
    inventory = Inventory[Item]()
    inventory.add_item(Item("apple", 10))
    print(inventory.get_quantity("apple"))