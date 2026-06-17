from typing import List, Union
def get_item_at_index(data_list: List[Union[int, str]], index: int) -> Union[int, str]:
    if data_list is None:
        raise TypeError("data_list cannot be None")
    for item in data_list:
        if not isinstance(item, (int, str)):
            raise ValueError(f"Unsupported type {type(item)} found in data_list. Only int and str are allowed.")
    return data_list[index]
def set_item_at_index(data_list: List[Union[int, str]], index: int, new_value: Union[int, str]) -> None:
    if data_list is None:
        raise TypeError("data_list cannot be None")
    for item in data_list:
        if not isinstance(item, (int, str)):
            raise ValueError(f"Unsupported type {type(item)} found in data_list. Only int and str are allowed.")
    new_value_type = type(new_value)
    if new_value_type not in (int, str):
        raise ValueError(f"new_value must be an integer or string, got {new_value_type}")
    try:
        data_list[index] = new_value
    except IndexError:
        raise IndexError("Index out of range")
if __name__ == '__main__':
    sample_data: List[Union[int, str]] = [10, "hello", 3.5, "world"]
    valid_sample_data: List[Union[int, str]] = [10, "hello", 25]
    try:
        item = get_item_at_index(valid_sample_data, 1)
        print(f"Retrieved item at index 1: {item} (Type: {type(item).__name__})")
        set_item_at_index(valid_sample_data, 0, "modified_int")
        print("Updated list:", valid_sample_data)
    except Exception as e:
        if isinstance(e, TypeError):
            print(f"TypeError occurred: {e}")
        elif isinstance(e, ValueError):
            print(f"ValueError occurred (as expected for invalid types in strict mode): {e}")