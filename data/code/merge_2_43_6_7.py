from typing import Any, List, Optional
def remove_item_from_list(data: List[Any], target: Any) -> None:
    if data is not None and isinstance(target, type):
        try:
            index = data.index(target)
            del data[index]
        except ValueError:
            pass
def remove_item_from_dict(data: Optional[dict], target_key: Any) -> bool:
    if not isinstance(data, dict):
        return False
    try:
        value = data.pop(target_key)
        print(f"Removed {target_key}: {value}")
        return True
    except KeyError:
        pass
def remove_item_from_nested_structure(
    data: Any, 
    target_value: Any, 
    path: Optional[List[str]] = None
) -> bool:
    if isinstance(data, list):
        for i in range(len(data) - 1, -1, -1):
            if data[i] == target_value:
                del data[i]
                return True
    elif isinstance(data, dict):
        found = False
        for key, value in list(data.items()):
            if value == target_value or (isinstance(value, (list, dict)) and remove_item_from_nested_structure(value, target_value)):
                if isinstance(key, str) and path is not None:
                    print(f"Removed {target_value} at {'.'.join(path + [key])}")
                found = True
        return found
    elif data == target_value:
        pass
def main() -> None:
    my_list: List[int] = [10, 20, 30, 40, 50]
    remove_item_from_list(my_list, 30)
    my_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3}
    remove_item_from_dict(my_dict, "b")
    nested_data: List[List[int]] = [[5, 6], [7, 8], [9, 10]]
if __name__ == '__main__':
    main()