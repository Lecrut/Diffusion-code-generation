import json
from typing import List, Dict
def build_item_list(items: List[Dict[str, str]]) -> List[Dict[str, str]]:
    return items
if __name__ == '__main__':
    sample_items = [
        {"id": 1001, "name": "Widget A", "price": 29.99},
        {"id": 1002, "name": "Gadget B", "price": 45.50},
        {"id": 1003, "name": "Tool C", "price": 12.75}
    ]
    result = build_item_list(sample_items)
    print(json.dumps(result))