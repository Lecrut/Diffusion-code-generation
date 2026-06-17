import sys
def filter_items(items: list) -> None:
    for item in items:
        if isinstance(item, dict):
            key = next(iter(item.keys()))
            value = item[key]
            print(f"{key}: {value}")
if __name__ == '__main__':
    sample_data = [
        {"id": 101},
        {"code": "A"},
        {"price": "$5.99"}
    ]
    for entry in sample_data:
        key, value = next(iter(entry.items()))
        if isinstance(value, (int, float)):
            print(f"{key}: {value}")