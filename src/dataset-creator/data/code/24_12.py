from typing import List, Dict
def build_item_list() -> List[Dict[str, str]]:
    items = [
        {"id": 1001, "name": "Laptop", "category": "Electronics"},
        {"id": 1002, "name": "Desk Chair", "category": "Furniture"},
        {"id": 1003, "name": "Wireless Mouse", "category": "Accessories"},
        {"id": 1004, "name": "Standing Desk", "category": "Furniture"},
    ]
    return items
if __name__ == '__main__':
    item_list = build_item_list()
    print(item_list)