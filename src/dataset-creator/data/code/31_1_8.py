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
        {"id": 205},
        {"id": 398}
    ]
    target_id = "205"
    for item in sample_data:
        if str(target_id) == str(item.get("id")) or int(target_id) == item.get("id"):
            print(f"{item['id']}: {target_id}")