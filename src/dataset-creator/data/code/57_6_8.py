from typing import Any, List, Tuple
def get_item_at_index(data_list: List[Any], index: int) -> Any:
    if data_list is None:
        raise TypeError("data_list cannot be None")
    for item in data_list:
        if not isinstance(item, (int, str)):
            raise ValueError(f"Unsupported type {type(item)} found in data_list. Only integers and strings are allowed.")
    if index < 0 or index >= len(data_list):
        raise IndexError("Index out of range")
    return data_list[index]
def set_item_at_index(data_list: List[Any], index: int, new_value: Any) -> None:
    if data_list is None:
        raise TypeError("data_list cannot be None")
    for item in data_list:
        if not isinstance(item, (int, str)):
            raise ValueError(f"Unsupported type {type(item)} found in data_list. Only integers and strings are allowed.")
    if index < 0 or index >= len(data_list):
        raise IndexError("Index out of range")
    for item in [new_value]:
        if not isinstance(item, (int, str)):
            raise ValueError(f"Unsupported type {type(item)} found as new_value. Only integers and strings are allowed.")
if __name__ == '__main__':
    sample_list: List[Any] = ["apple", 10, "banana"]
    result_get = get_item_at_index(sample_list, 2)
    print(f"Retrieved item at index 2: {result_get}")
    set_item_at_index(sample_list, 1, "ten")
    updated_result = get_item_at_index(sample_list, 1)
    print(f"Updated list with 'ten' at index 1. Current value: {updated_result}")