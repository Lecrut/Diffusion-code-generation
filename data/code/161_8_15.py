from dataclasses import dataclass

@dataclass
class Item:
    name: str
    quantity: int

def create_item_list():
    return [
        Item("apple", 10),
        Item("banana", 20),
        Item("cherry", 30),
        Item("date", 40)
    ]

if __name__ == '__main__':
    item_list = create_item_list()
    for item in item_list:
        print(f"{item.name}: {item.quantity}")