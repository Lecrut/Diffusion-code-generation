from dataclasses import dataclass
@dataclass(frozen=True)
class Item:
    name: str
    price: float
    quantity: int
def create_item_list() -> list[Item]:
    return [
        Item(name="Laptop", price=999.99, quantity=1),
        Item(name="Mouse", price=25.50, quantity=5),
        Item(name="Keyboard", price=75.00, quantity=3)
    ]
def calculate_total_price(items: list[Item]) -> float:
    return sum(item.price * item.quantity for item in items)
if __name__ == '__main__':
    inventory = create_item_list()
    total_cost = calculate_total_price(inventory)
    print(f"Total Cost: {total_cost:.2f}")