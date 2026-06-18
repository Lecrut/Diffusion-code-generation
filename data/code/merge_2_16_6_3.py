from typing import Any, List
def count_elements(data: Any) -> int:
    if isinstance(data, list):
        return sum(count_elements(item) for item in data)
    elif isinstance(data, dict):
        return len(data)
    else:
        return 0
if __name__ == '__main__':
    flat_list = [1, 2, 3]
    nested_structure = {
        'a': [4, {'b': [5, 6]}],
        'c': [[7, 8]]
    }
    print(f"Flat list count: {count_elements(flat_list)}")
    print(f"Nested structure count: {count_elements(nested_structure)}")