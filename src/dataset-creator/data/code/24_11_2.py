class ItemList:
    def __init__(self):
        self.items = []
    def add_item(self, name: str, price: float) -> bool:
        if not isinstance(name, str) or len(name.strip()) == 0:
            return False
        try:
            price = float(price)
            if price < 0:
                raise ValueError("Price must be non-negative.")
        except (ValueError, TypeError):
            return False
        self.items.append({"name": name.strip(), "price": round(price, 2)})
        return True
    def get_items(self) -> list[dict]:
        return [item.copy() for item in self.items]
if __name__ == '__main__':
    inventory = ItemList()
    sample_data = [
        ("Laptop", 999.50),
        ("Mouse", 25.00),
        (123, -10.00)
    ]
    for name, price in sample_data:
        inventory.add_item(name, price)
    print(inventory.get_items())