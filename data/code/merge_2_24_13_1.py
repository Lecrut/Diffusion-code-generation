class Item:
    def __init__(self, name: str, price: float, quantity: int):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise TypeError("Name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        self._name = name.strip()
        self.price = float(price)
        self.quantity = quantity
    @property
    def total(self) -> float:
        return round(self.price * self.quantity, 2)
class ItemList:
    def __init__(self):
        self._items = []
    @staticmethod
    def _validate_item(item_data: dict) -> None:
        required_keys = {'name', 'price', 'quantity'}
        if not isinstance(item_data, dict):
            raise TypeError("Item data must be a dictionary.")
        missing_keys = required_keys - set(item_data.keys())
        if missing_keys:
            raise ValueError(f"Missing required keys: {missing_keys}")
    def add_item(self, item_data: dict) -> None:
        self._validate_item(item_data)
        try:
            new_item = Item(**item_data)
            self._items.append(new_item)
        except (TypeError, ValueError) as e:
            raise RuntimeError(f"Failed to add item due to validation error: {e}")
    def get_total_value(self) -> float:
        return round(sum(item.total for item in self._items), 2)
if __name__ == '__main__':
    list_instance = ItemList()
    sample_items = [
        {'name': 'Laptop', 'price': 999.50, 'quantity': 1},
        {'name': 'Mouse', 'price': 25.00, 'quantity': 3},
        {'name': 'Keyboard', 'price': 75.99, 'quantity': 2}
    ]
    for item_data in sample_items:
        list_instance.add_item(item_data)
    print(f"Total Value of Items: ${list_instance.get_total_value():.2f}")