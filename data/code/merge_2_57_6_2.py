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
    new_value_type = type(new_value)
    existing_types = [type(x) for x in data_list]
    if set(existing_types).difference({new_value_type}):
        raise TypeError("List contains mixed types that cannot be updated with the provided value")
    data_list[index] = new_value
if __name__ == '__main__':
    sample_data: List[Union[int, str]] = [10, "hello", 3.5, None]
    try:
        result = get_item_at_index(sample_data, 2)
        print(f"Retrieved item at index 2: {result}")
        set_item_at_index(sample_data, 2, 42)
        print("Item updated successfully")
        print(f"Updated list: {sample_data}")
    except Exception as e:
        if isinstance(e, TypeError):
            print(f"Type Error occurred: {e}")
        elif isinstance(e, ValueError):
            print(f"Value Error occurred: {e}")