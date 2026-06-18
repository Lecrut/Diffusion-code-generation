from typing import Any, List
def count_elements(data: Any) -> int:
    if isinstance(data, (list, tuple)):
        return sum(count_elements(item) for item in data)
    try:
        len(data)
        return 1 if not hasattr(data, '__iter__') or type(data).__name__ == 'str' else count_elements(list(data))
    except TypeError:
        pass
    return 0
if __name__ == '__main__':
    flat_list = [1, 2, 3]
    nested_structure = [[1, 2], [3, [4, 5]], 6]
    result_flat = count_elements(flat_list)
    result_nested = count_elements(nested_structure)
    print(result_flat)
    print(result_nested)