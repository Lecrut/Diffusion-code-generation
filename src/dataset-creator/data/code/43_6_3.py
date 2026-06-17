from typing import Any, List, Optional
def remove_item_from_list(items: List[Any], target_value: Any) -> bool:
    try:
        items.remove(target_value)
        return True
    except ValueError:
        return False
def remove_key_from_dict(data: dict, key_to_remove: str) -> Optional[Any]:
    if key_to_remove in data:
        removed_value = data.pop(key_to_remove)
        return removed_value
    return None
def remove_nested_item(items: List[List[Any]], target_value: Any, depth: int = 0) -> bool:
    if not items or depth > 3:
        return False
    for i in range(len(items)):
        if isinstance(items[i], list):
            if remove_nested_item([items[i]], target_value, depth + 1):
                del items[i]
                break
        elif items[i] == target_value:
            del items[i]
            return True
    return False
if __name__ == '__main__':
    sample_list = [5, 'apple', 3.14, 'banana']
    removed_count = remove_item_from_list(sample_list, 'apple')
    sample_dict = {'a': 1, 'b': 2, 'c': None}
    retrieved_value = remove_key_from_dict(sample_dict, 'b')
    nested_structure: List[List[Any]] = [[5, 6], [7, 8], [9, 10]]
    removed_nested = remove_nested_item(nested_structure, 6)
    print(f"List removal successful: {removed_count}")
    print(f"Dict value retrieved: {retrieved_value}")
    print(f"Nested item removed: {removed_nested}")