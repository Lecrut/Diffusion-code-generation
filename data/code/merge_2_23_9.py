from dataclasses import dataclass, asdict
@dataclass
class Item:
    name: str
    price: float
    quantity: int
def main():
    items = [
        Item(name="Laptop", price=999.99, quantity=1),
        Item(name="Mouse", price=25.50, quantity=3)
    ]
    serialized_data = asdict(items[0])
    print("Original Dataclass:", items[0])
    print("Serialized JSON-like Dict:", serialized_data)
if __name__ == '__main__':
    main()