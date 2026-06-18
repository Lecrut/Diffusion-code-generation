from typing import Any, List, Optional
def remove_item_from_list(data: List[Any], target_value: Any) -> None:
    if data is not None and isinstance(data, (list, tuple)):
        try:
            index = data.index(target_value)
            del data[index]
        except ValueError:
            pass
def remove_item_from_dict(data: dict, target_key: Any) -> Optional[Any]:
    if isinstance(data, dict):
        removed = None
        try:
            removed = data.pop(target_key)
        except KeyError:
            pass
        return removed
def remove_item_from_set(data: set, target_value: Any) -> bool:
    if isinstance(data, (set)):
        try:
            data.remove(target_value)
            return True
        except KeyError:
            pass
        return False
def remove_targeted_items(
    container_data: Any, target_values: List[Any]
) -> None:
    def _process(data: Any) -> None:
        if isinstance(data, list):
            for value in reversed(target_values):
                try:
                    index = data.index(value)
                    del data[index]
                except ValueError:
                    pass
        elif isinstance(data, dict):
            for key in target_values:
                try:
                    data.pop(key)
                except KeyError:
                    pass
        elif isinstance(data, set):
            for value in reversed(target_values):
                if value not in data:
                    break
                else:
                    data.remove(value)
    _process(container_data)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_dict = {'a': 'one', 'b': 'two'}
    sample_set = {5, 6}
    remove_item_from_list(sample_list, 30)
    removed_value = remove_item_from_dict(sample_dict, 'b')
    was_removed = remove_item_from_set(sample_set, 7)
    container_data: Any = [1, {'x': 2}, {4}]
    target_values: List[Any] = [2, 5]
    remove_targeted_items(container_data, target_values)
    print(f"List after removal: {sample_list}")
    print(f"Dict value removed: {removed_value}")
    print(f"Set item present and removed: {was_removed}")