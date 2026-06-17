from typing import Any, List
def get_item_at_index(data_list: List[Any], index: int) -> Any:
    if data_list is None:
        raise TypeError("data_list cannot be None")
    for item in data_list:
        if not isinstance(item, (int, str)):
            raise ValueError(f"Unsupported type {type(item).__name__} found in list. Only integers and strings are allowed.")
    return data_list[index]
def set_item_at_index(data_list: List[Any], index: int, new_value: Any) -> None:
    if data_list is None:
        raise TypeError("data_list cannot be None")
    for item in data_list:
        if not isinstance(item, (int, str)):
            raise ValueError(f"Unsupported type {type(item).__name__} found in list. Only integers and strings are allowed.")
    if not isinstance(new_value, (int, str)):
        raise TypeError("new_value must be an integer or string")
    data_list[index] = new_value
if __name__ == '__main__':
    sample_data: List[Any] = [10, "hello", 3.5, None]
    try:
        result = get_item_at_index(sample_data, 2)
        print(f"Retrieved item at index 2: {result}")
        set_item_at_index(sample_data, 2, "modified")
        print("Updated list:", sample_data)
    except (TypeError, ValueError) as e:
        print(f"Error occurred: {e}")