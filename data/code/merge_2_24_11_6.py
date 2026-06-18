class ItemList:
    def __init__(self):
        self.items = []
    def add_item(self, name: str, price: float) -> bool:
        if not isinstance(name, str) or len(name.strip()) == 0:
            return False
        try:
            price_value = float(price)
            if price_value < 0:
                raise ValueError("Price cannot be negative")
            self.items.append({
                "name": name.strip(),
                "price": round(price_value, 2),
                "id": len(self.items) + 1
            })
            return True
        except (ValueError, TypeError):
            return False
    def get_total_price(self) -> float:
        return sum(item["price"] for item in self.items)
if __name__ == '__main__':
    inventory = ItemList()
    sample_data = [
        ("Laptop", 999.50),
        ("Mouse", 25.00),
        ("Keyboard", 75.99),
        (123, -10.00)
    ]
    for name, price in sample_data:
        inventory.add_item(name, price)
    print(f"Total Inventory Value: ${inventory.get_total_price():.2f}")