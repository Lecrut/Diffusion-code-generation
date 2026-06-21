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
        self.items: dict[str, T] = {}

    def add_item(self, item: T) -> None:
        if not isinstance(item, Item):
            raise ValueError("Item must be an instance of Item")
        if item.name in self.items:
            self.items[item.name].quantity += item.quantity
        else:
            self.items[item.name] = item

    def get_item(self, name: str) -> T:
        if name not in self.items:
            raise KeyError(f"Item '{name}' not found")
        return self.items[name]

if __name__ == '__main__':
    inventory = Inventory[Item]()
    item1 = Item("apple", 5)
    item2 = Item("banana", 3)
    inventory.add_item(item1)
    inventory.add_item(item2)
    print(inventory.get_item("apple"))
    print(inventory.get_item("banana"))