from typing import List, Union
def get_item_at_index(data_list: List[Union[int, str]], index: int) -> Union[int, str]:
    if data_list is None:
        raise TypeError("data_list cannot be None")
    for item in data_list:
        if not isinstance(item, (int, str)):
            raise ValueError(f"Unsupported type {type(item).__name__} found in list. Only int and str are allowed.")
    return data_list[index]
def set_item_at_index(data_list: List[Union[int, str]], index: int, new_value: Union[int, str]) -> None:
    if data_list is None:
        raise TypeError("data_list cannot be None")
    for item in data_list:
        if not isinstance(item, (int, str)):
            raise ValueError(f"Unsupported type {type(item).__name__} found in list. Only int and str are allowed.")
    if new_value is None or not isinstance(new_value, (int, str)):
        raise TypeError("new_value must be an integer or string")
    data_list[index] = new_value
if __name__ == '__main__':
    sample_data: List[Union[int, str]] = [10, "hello", 3.5, "world"]
    try:
        item = get_item_at_index(sample_data, 2)
        print(f"Retrieved item at index 2: {item}")
        set_item_at_index(sample_data, 2, "modified")
        print("Updated list:", sample_data)
    except Exception as e:
        print(f"Error occurred: {e}")