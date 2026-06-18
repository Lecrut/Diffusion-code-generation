import json
from datetime import datetime
from typing import List, Dict
class ItemProcessor:
    def __init__(self):
        self.items_data = [
            {"id": 1001, "name": "Widget A", "price": 29.99},
            {"id": 1002, "name": "Gadget B", "price": 49.50},
            {"id": 1003, "name": "Tool C", "price": 15.75}
        ]
    def generate_item_list(self) -> List[Dict]:
        return self.items_data.copy()
def format_output(items: List[Dict]) -> str:
    output = []
    for item in items:
        timestamp = datetime.now().isoformat(timespec='milliseconds')
        line = f"[{timestamp}] ID:{item['id']} | {item['name']}: ${item['price']:.2f}"
        output.append(line)
    return "\n".join(output)
if __name__ == '__main__':
    processor = ItemProcessor()
    items = processor.generate_item_list()
    print(format_output(items))