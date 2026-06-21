from typing import Generic, TypeVar, Dict

T = TypeVar('T')

class Item(Generic[T]):
    def __init__(self, name: str, quantity: T):
        self.name = name
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.items: Dict[str, Item] = {}

    def add_item(self, item: Item) -> None:
        if not isinstance(item, Item):
            raise ValueError("Item must be an instance of Item")
        if item.name in self.items:
            self.items[item.name].quantity += item.quantity
        else:
            self.items[item.name] = item

    def get_quantity(self, name: str) -> T:
        return self.items.get(name, Item("", 0)).quantity

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item(Item("apple", 10))
    print(inventory.get_quantity("apple"))