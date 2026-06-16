from typing import Any, List
def count_elements(data: Any) -> int:
    if isinstance(data, list):
        return sum(count_elements(item) for item in data)
    elif isinstance(data, dict):
        total = 0
        for value in data.values():
            total += count_elements(value)
        return total
    else:
        return 1
if __name__ == '__main__':
    flat_list = [1, 'a', True]
    nested_structure = {
        "outer_key": [10, 20],
        "inner_dict": {"key_a": "value", "key_b": [30]},
        "simple_value": None
    }
    flat_count = count_elements(flat_list)
    nested_count = count_elements(nested_structure)
    print(f"Flat list elements: {flat_count}")
    print(f"Nested structure elements: {nested_count}")