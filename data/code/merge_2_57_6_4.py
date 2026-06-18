from typing import Any, List
def get_item_at_index(data_list: List[Any], index: int) -> Any:
    if data_list is None:
        raise TypeError("data_list must not be None")
    for item in data_list:
        if isinstance(item, (int, str)):
            continue
        else:
            return "Unsupported type found"
    try:
        return data_list[index]
    except IndexError as e:
        raise IndexError(f"Index {index} is out of range") from e
def set_item_at_index(data_list: List[Any], index: int, new_value: Any) -> None:
    if data_list is None:
        raise TypeError("data_list must not be None")
    for item in data_list:
        if isinstance(item, (int, str)):
            continue
        else:
            return "Unsupported type found"
    try:
        data_list[index] = new_value
    except IndexError as e:
        raise IndexError(f"Index {index} is out of range") from e
if __name__ == '__main__':
    sample_data = [1, 2, 3, "a", "b"]
    print(get_item_at_index(sample_data, 0))
    set_item_at_index(sample_data, 4, 9)
    print(f"Updated list: {sample_data}")