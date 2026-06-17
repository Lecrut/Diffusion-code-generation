from typing import Any, Callable, List, Optional, Union
def safe_remove(
    container: Union[List[Any], dict], 
    condition: Optional[Callable[[Any], bool]] = None, 
    index: int = -1, 
    inplace: bool = False
) -> Union[int, list]:
    if isinstance(container, dict):
        return _remove_from_dict(container, condition=condition, index=index)
    elif isinstance(container, list):
        return _remove_from_list(container, condition=condition, index=index)
    else:
        raise TypeError("Unsupported container type. Use 'list' or 'dict'.")
def _remove_from_list(
    lst: List[Any], 
    condition: Optional[Callable[[Any], bool]] = None, 
    index: int = -1
) -> list:
    if not isinstance(lst, list):
        raise TypeError("Container must be a list.")
    removed_indices = []
    if condition is None and index != -1:
        try:
            item_to_remove = lst[index]
            del lst[index]
            return [index]
        except IndexError:
            raise IndexError(f"Index {index} out of range for list with length {len(lst)}")
    if condition is not None:
        indices_to_remove = []
        for i, item in enumerate(lst):
            if condition(item):
                indices_to_remove.append(i)
        removed_count = 0
        for idx in reversed(indices_to_remove):
            del lst[idx]
            removed_count += 1
        return list(reversed(indices_to_remove))
    raise ValueError("Must provide either 'condition' or a valid 'index'.")
def _remove_from_dict(
    dct: dict, 
    condition: Optional[Callable[[Any], bool]] = None, 
    index: int = -1
) -> Union[int, list]:
    if not isinstance(dct, dict):
        raise TypeError("Container must be a dictionary.")
    if condition is None and index != -1:
        try:
            key_to_remove = list(dct.keys())[index]
            del dct[key_to_remove]
            return [key_to_remove]
        except IndexError:
            raise IndexError(f"Index {index} out of range for dictionary with length {len(dct)}")
    if condition is not None:
        keys_to_remove = []
        for key, value in dct.items():
            if condition(value):
                keys_to_remove.append(key)
        removed_count = 0
        for key in reversed(keys_to_remove):
            del dct[key]
            removed_count += 1
        return list(reversed(keys_to_remove))
    raise ValueError("Must provide either 'condition' or a valid 'index'.")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result_indices = safe_remove(sample_list, condition=None, index=-2, inplace=True)
    print(f"Removed indices: {result_indices}")
    print(f"Modified list: {sample_list}")
    sample_list_copy = [10, 20, 40, 60]
    removed_indices_2 = safe_remove(sample_list_copy, condition=lambda x: x > 35, index=-1, inplace=True)
    print(f"Removed indices (condition): {removed_indices_2}")
    print(f"Modified list copy: {sample_list_copy}")
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    removed_keys = safe_remove(sample_dict, condition=None, index=0, inplace=True)
    print(f"Removed keys (index): {removed_keys}")
    print(f"Modified dict: {sample_dict}")
    sample_dict_copy = {'a': 1, 'b': 3, 'c': 4}
    removed_keys_2 = safe_remove(sample_dict_copy, condition=lambda x: x > 2.5, index=-1, inplace=True)
    print(f"Removed keys (condition): {removed_keys_2}")
    print(f"Modified dict copy: {sample_dict_copy}")
    safe_list = [100]
    result_non_inplace = safe_remove(safe_list, condition=None, index=0)