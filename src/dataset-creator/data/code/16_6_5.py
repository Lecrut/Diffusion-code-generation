from typing import Any, List
def count_elements(data: Any) -> int:
    if isinstance(data, dict):
        return sum(count_elements(value) for value in data.values())
    elif isinstance(data, (list, tuple)):
        return sum(count_elements(item) for item in data)
    else:
        return 1
if __name__ == '__main__':
    flat_list = [1, 'a', True]
    nested_structure = {
        "outer": [10, {"inner": [20, 30]}, None],
        "items": ["x", "y"]
    }
    print(f"Flat list count: {count_elements(flat_list)}")
    print(f"Nested structure count: {count_elements(nested_structure)}")