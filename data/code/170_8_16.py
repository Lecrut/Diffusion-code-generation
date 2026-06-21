from typing import Generic, TypeVar, List

T = TypeVar('T')

class Item(Generic[T]):
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def __eq__(self, other):
        return (self.name == other.name) and (self.quantity == other.quantity)

class Inventory(Generic[T]):
    def __init__(self):
        self.items: List[Item[T]] = []

    def add_item(self, item: Item[T]) -> None:
        if not isinstance(item, Item):
            raise ValueError("Invalid item type")
        self.items.append(item)

    def remove_item(self, item_name: str) -> None:
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return
        raise KeyError(f"Item '{item_name}' not found")

    def get_inventory(self) -> List[Item[T]]:
        return self.items

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item(Item("apple", 10))
    inventory.add_item(Item("banana", 5))
    print(inventory.get_inventory())
    inventory.remove_item("apple")
    print(inventory.get_inventory())