from typing import Generic, TypeVar, List

T = TypeVar('T')

class Item(Generic[T]):
    def __init__(self, name: str, quantity: T):
        self.name = name
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"{self.name}: {self.quantity}"

class Inventory(Generic[T]):
    def __init__(self):
        self.items: List[Item[T]] = []

    def add_item(self, item: Item[T]) -> None:
        self.items.append(item)

    def get_items(self) -> List[Item[T]]:
        return self.items

if __name__ == '__main__':
    inventory = Inventory[int]()
    inventory.add_item(Item('apples', 10))
    inventory.add_item(Item('oranges', 5))
    print(inventory.get_items())