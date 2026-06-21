from typing import Generic, TypeVar
T = TypeVar('T')

class Item(Generic[T]):

    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def update_quantity(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise ValueError('Amount must be an integer')
        self.quantity += amount

class Inventory(Generic[T]):

    def __init__(self):
        self.items = {}

    def add_item(self, item: Item[T]) -> None:
        if not isinstance(item, Item):
            raise ValueError('Item must be an instance of Item')
        if item.name in self.items:
            self.items[item.name].update_quantity(item.quantity)
        else:
            self.items[item.name] = item

    def get_item(self, name: str) -> Item[T]:
        if not isinstance(name, str):
            raise ValueError('Name must be a string')
        return self.items.get(name)
if __name__ == '__main__':
    inventory = Inventory()
    book = Item('Book', 10)
    inventory.add_item(book)
    print(inventory.get_item('Book').quantity)