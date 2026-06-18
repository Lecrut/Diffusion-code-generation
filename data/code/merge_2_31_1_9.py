import sys
def filter_items(items: list) -> None:
    for item in items:
        if isinstance(item, dict):
            key = next(iter(item.keys()))
            value = item[key]
            print(f"{key}: {value}")
        else:
            print(item)
if __name__ == '__main__':
    data_list = [
        {"id": 101},
        "apple",
        {"code": "A"},
        None,
        ["banana"],
        {"key": "target"}
    ]
    for item in data_list:
        if isinstance(item, dict):
            keys = list(item.keys())
            value_to_match = next(iter(keys))
            actual_value = item[value_to_match]
            print(f"{value_to_match}: {actual_value}")