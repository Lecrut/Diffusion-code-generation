from typing import Any, List
def get_item_at_index(data_list: List[Any], index: int) -> Any:
    if data_list is None:
        raise TypeError("data_list cannot be None")
    for item in data_list:
        if not isinstance(item, (int, str)):
            raise ValueError(f"Unsupported type {type(item).__name__} found in list. Only int and str are allowed.")
    return data_list[index]
def set_item_at_index(data_list: List[Any], index: int, new_value: Any) -> None:
    if data_list is None:
        raise TypeError("data_list cannot be None")
    for item in data_list:
        if not isinstance(item, (int, str)):
            raise ValueError(f"Unsupported type {type(item).__name__} found in list. Only int and str are allowed.")
    new_value_type = type(new_value)
    existing_types_in_data = set(type(x) for x in data_list)
    if not isinstance(new_value, (int, str)):
        raise ValueError(f"new_value must be an integer or string, got {type(new_value).__name__}")
    if new_value_type != int and new_value_type not in existing_types_in_data:
        raise ValueError("All items in the list must share a consistent type. Cannot mix types.")
    data_list[index] = new_value
if __name__ == '__main__':
    sample_list = [1, "hello", 42, "world"]
    print(get_item_at_index(sample_list, 0))
    set_item_at_index(sample_list, 3, "changed")
    print(f"Updated list: {sample_list}")