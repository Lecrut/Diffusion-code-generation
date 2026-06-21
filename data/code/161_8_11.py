from dataclasses import dataclass

@dataclass
class Item:
    name: str
    quantity: int

if __name__ == '__main__':
    sample_items = [
        Item("apple", 10),
        Item("banana", 5),
        Item("cherry", 20),
        Item("date", 3)
    ]
    for item in sample_items:
        print(f"{item.name}: {item.quantity}")