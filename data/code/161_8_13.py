from dataclasses import dataclass

@dataclass(frozen=True)
class Item:
    name: str
    quantity: int

class ItemList:
    ITEMS = [
        Item("apple", 10),
        Item("banana", 20),
        Item("cherry", 30),
        Item("date", 40),
    ]

    @staticmethod
    def display_items():
        for item in ItemList.ITEMS:
            print(f"{item.name}: {item.quantity}")

if __name__ == '__main__':
    ItemList.display_items()