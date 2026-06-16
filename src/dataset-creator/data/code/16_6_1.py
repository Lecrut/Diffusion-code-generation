from typing import Any, List
def count_elements(data: Any) -> int:
    if isinstance(data, list):
        return sum(count_elements(item) for item in data)
    return 1
if __name__ == '__main__':
    flat_list = [10, 20, 30]
    nested_structure = [[5], [6, [7]], 8]
    result_flat = count_elements(flat_list)
    result_nested = count_elements(nested_structure)
    print(result_flat)
    print(result_nested)