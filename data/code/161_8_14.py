from dataclasses import dataclass

@dataclass
class Item:
    name: str
    quantity: int

ITEMS = [
    Item("apple", 10),
    Item("banana", 20),
    Item("cherry", 30),
    Item("date", 40)
]

def print_items(items):
    for item in items:
        print(f"Item: {item.name}, Quantity: {item.quantity}")

if __name__ == '__main__':
    print_items(ITEMS)