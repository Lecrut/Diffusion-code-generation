from typing import Generic, TypeVar, List

T = TypeVar('T')

class Item(Generic[T]):
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

class Inventory(Generic[T]):
    def __init__(self):
        self.items: List[Item[T]] = []

    def add_item(self, item: Item[T]) -> None:
        self.items.append(item)

    def get_total_quantity(self) -> int:
        return sum(item.quantity for item in self.items)

if __name__ == '__main__':
    inventory = Inventory[str]()
    inventory.add_item(Item('apple', 10))
    inventory.add_item(Item('banana', 5))
    print(inventory.get_total_quantity())