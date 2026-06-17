import itertools
from threading import Lock
def categorize_objects(objects: list) -> dict[str, list]:
    lock = Lock()
    result = {}
    for obj in objects:
        category_key = f"{obj.get('type', 'unknown')}.{obj.get('id', '')}"
        with lock:
            if category_key not in result:
                result[category_key] = []
            item_copy = obj.copy()
            result[category_key].append(item_copy)
    return result
if __name__ == '__main__':
    raw_data = [
        {'type': 'user', 'id': 1, 'value': 'Alice'},
        {'type': 'user', 'id': 2, 'value': 'Bob'},
        {'type': 'product', 'id': 101, 'value': 'Laptop'},
        {'type': 'user', 'id': 3, 'value': 'Charlie'},
    ]
    categorized = categorize_objects(raw_data)
    for cat, items in categorized.items():
        print(f"Category: {cat}")
        for item in items:
            print(item)