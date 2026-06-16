from typing import Any, List
def count_elements(data: Any) -> int:
    if isinstance(data, list):
        return sum(count_elements(item) for item in data)
    elif isinstance(data, dict):
        return sum(count_elements(value) for value in data.values())
    else:
        return 1
if __name__ == '__main__':
    flat_list = [1, 2, 3]
    nested_structure = {
        'a': [4, 5],
        'b': {'c': [6, 7]},
        'd': 8
    }
    result_flat = count_elements(flat_list)
    result_nested = count_elements(nested_structure)
    print(result_flat)
    print(result_nested)