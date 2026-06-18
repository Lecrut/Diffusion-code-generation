from typing import Any, List, Union
def get_item_at_index(data_list: List[Union[int, str]], index: int) -> Union[int, str]:
    if data_list is None:
        raise TypeError("data_list cannot be None")
    for item in data_list:
        if not isinstance(item, (int, str)):
            raise ValueError(f"Unsupported type {type(item)} found in list. Only integers and strings are allowed.")
    return data_list[index]
def set_item_at_index(data_list: List[Union[int, str]], index: int, new_value: Union[int, str]) -> None:
    if data_list is None:
        raise TypeError("data_list cannot be None")
    for item in data_list:
        if not isinstance(item, (int, str)):
            raise ValueError(f"Unsupported type {type(item)} found in list. Only integers and strings are allowed.")
    new_value_type = type(new_value)
    if new_value_type not in (int, str):
        raise TypeError("new_value must be an integer or a string")
    data_list[index] = new_value
if __name__ == '__main__':
    sample_data: List[Union[int, str]] = [10, "hello", 3.5, "world"]
    try:
        result = get_item_at_index(sample_data, 2)
    except ValueError as e:
        print(f"Error retrieving item: {e}")
    valid_sample: List[Union[int, str]] = [10, "hello", 3, "world"]
    try:
        retrieved_item = get_item_at_index(valid_sample, 2)
        print(f"Retrieved item at index 2: {retrieved_item}")
        set_item_at_index(valid_sample, 2, 99)
        print("Updated list:", valid_sample)
    except Exception as e:
        print(f"Error during operations: {e}")