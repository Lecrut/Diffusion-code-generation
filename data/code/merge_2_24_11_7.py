import re
def validate_item(item: dict) -> bool:
    required_keys = {'name', 'price'}
    return all(key in item for key in required_keys) and isinstance(item.get('price'), (int, float))
class ItemListManager:
    def __init__(self):
        self.items = []
    def add_item(self, name: str, price: int | float) -> None:
        if not validate_item({'name': name, 'price': price}):
            raise ValueError("Invalid item data")
        self.items.append({'name': name, 'price': price})
    def get_items(self) -> dict[str, int | float]:
        return {item['name']: item['price'] for item in self.items}
if __name__ == '__main__':
    manager = ItemListManager()
    manager.add_item('Laptop', 999)
    manager.add_item('Mouse', 25.50)
    output_dict = manager.get_items()
    print(output_dict)