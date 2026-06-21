from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float
    quantity: int

if __name__ == '__main__':
    sample_items = [
        Item(name="Apple", price=0.5, quantity=10),
        Item(name="Banana", price=0.3, quantity=20),
        Item(name="Cherry", price=0.8, quantity=15)
    ]
    
    for item in sample_items:
        print(f"Item: {item.name}, Price: ${item.price}, Quantity: {item.quantity}")