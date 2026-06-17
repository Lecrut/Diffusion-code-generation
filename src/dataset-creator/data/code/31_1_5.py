import sys
def filter_items(items_list: list) -> None:
    for item in items_list:
        if isinstance(item, dict):
            key = next(iter(item.keys()))
            value = item[key]
            print(f"{key}: {value}")
if __name__ == '__main__':
    sample_data = [
        {"id": 101, "status": "active"},
        {"id": 102, "status": "inactive"},
        {"id": 103, "status": "active"}
    ]
    filter_items(sample_data)