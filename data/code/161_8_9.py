from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float
    quantity: int

if __name__ == '__main__':
    items = [
        Item(name="Apple", price=0.5, quantity=10),
        Item(name="Banana", price=0.3, quantity=20),
        Item(name="Cherry", price=1.0, quantity=5)
    ]
    for item in items:
        print(f"{item.name}: ${item.price * item.quantity:.2f}")