from dataclasses import dataclass

@dataclass
class Item:
    name: str
    quantity: int

def display_items(items):
    for item in items:
        print(f"{item.name}: {item.quantity}")

if __name__ == '__main__':
    sample_data = [
        ("apple", 10),
        ("banana", 20),
        ("cherry", 30),
        ("date", 40)
    ]
    item_list = [Item(name, quantity) for name, quantity in sample_data]
    display_items(item_list)