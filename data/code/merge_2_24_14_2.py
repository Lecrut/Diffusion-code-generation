import json
from datetime import datetime
from typing import List, Dict
class ItemListGenerator:
    def __init__(self):
        self.items: List[Dict[str, any]] = []
    def add_item(self, name: str, description: str, price: float) -> None:
        entry = {
            "id": len(self.items),
            "name": name,
            "description": description,
            "price": round(price, 2),
            "created_at": datetime.now().isoformat()
        }
        self.items.append(entry)
    def get_item_list(self) -> List[Dict[str, any]]:
        return self.items.copy()
def generate_sample_data(generator: ItemListGenerator) -> None:
    generator.add_item("Laptop Pro X", "High-performance laptop for professionals", 2499.99)
    generator.add_item("Wireless Headphones", "Noise-cancelling over-ear headphones", 199.50)
    generator.add_item("Smart Thermostat", "WiFi-enabled climate control system", 89.99)
    generator.add_item("LED Desk Lamp", "Adjustable brightness and color temperature", 45.75)
if __name__ == '__main__':
    item_list = ItemListGenerator()
    generate_sample_data(item_list)
    output_json = json.dumps(
        {
            "generated_at": datetime.now().isoformat(),
            "total_items": len(item_list.get_item_list()),
            "items": item_list.get_item_list()
        },
        indent=2,
        sort_keys=True                                                                
    )
    print(output_json)