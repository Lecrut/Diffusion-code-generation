import sys
def filter_items(items: list) -> None:
    for item in items:
        if isinstance(item, dict):
            key = next(iter(item))
            value = item[key]
            print(f"{key}: {value}")
if __name__ == '__main__':
    sample_data = [
        {"id": 101, "status": "active"},
        {"id": 102, "status": "inactive"},
        {"id": 103, "status": "pending"}
    ]
    target_status = "active"
    for item in sample_data:
        key = next(iter(item))
        value = item[key]
        if str(value) == str(target_status):
            print(f"{key}: {value}")