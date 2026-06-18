import re
def validate_item(item: dict) -> bool:
    required_keys = {'name', 'price'}
    return all(key in item for key in required_keys) and isinstance(item['price'], (int, float))
class ItemListManager:
    def __init__(self):
        self.items = []
    def add_item(self, name: str, price: int | float) -> None:
        if not validate_item({'name': name, 'price': price}):
            raise ValueError("Invalid item data")
        self.items.append({'name': name, 'price': price})
    def get_items(self) -> list[dict]:
        return [item.copy() for item in self.items]
if __name__ == '__main__':
    manager = ItemListManager()
    manager.add_item('Laptop', 999.50)
    manager.add_item('Mouse', 25)
    items_list = manager.get_items()
    for item in items_list:
        print(f"{item['name']}: ${item['price']}")