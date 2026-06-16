import json
from typing import List, Dict
def build_item_list() -> List[Dict[str, str]]:
    items = [
        {"id": 1001, "name": "Laptop", "category": "Electronics"},
        {"id": 1002, "name": "Headphones", "category": "Accessories"},
        {"id": 1003, "name": "Desk Chair", "category": "Furniture"},
    ]
    return items
if __name__ == '__main__':
    result = build_item_list()
    print(json.dumps(result))