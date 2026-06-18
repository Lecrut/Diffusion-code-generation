import json
from typing import List, Dict
class ItemListGenerator:
    def __init__(self):
        self.items = []
    def add_item(self, name: str, price: float) -> None:
        if not isinstance(name, str) or not isinstance(price, (int, float)):
            raise ValueError("Invalid item data")
        self.items.append({"name": name, "price": price})
    def generate_report(self) -> List[Dict]:
        return sorted(self.items, key=lambda x: x["price"])
def create_sample_data() -> ItemListGenerator:
    generator = ItemListGenerator()
    sample_items = [
        ("Laptop", 999.99),
        ("Mouse", 25.50),
        ("Keyboard", 75.00),
        ("Monitor", 350.00)
    ]
    for name, price in sample_items:
        generator.add_item(name, price)
    return generator
if __name__ == '__main__':
    item_generator = create_sample_data()
    final_list = item_generator.generate_report()
    output_json = json.dumps(final_list, indent=2)
    print(output_json)