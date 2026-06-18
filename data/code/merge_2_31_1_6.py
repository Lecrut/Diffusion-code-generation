import json
def filter_items(items: list[dict], key_name: str, target_value) -> list[str]:
    return [item[key_name] for item in items if item.get(key_name) == target_value]
if __name__ == '__main__':
    sample_data = [
        {"id": 101, "status": "active", "user": "alice"},
        {"id": 102, "status": "inactive", "user": "bob"},
        {"id": 103, "status": "active", "user": "charlie"},
    ]
    target = "active"
    result_ids = filter_items(sample_data, "status", target)
    print(f"\nItems with status '{target}':")
    for item_id in result_ids:
        print(item_id)