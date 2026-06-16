from typing import Any, List, Dict, TypeVar, Union
T = TypeVar('T')
def check_item_in_list(items: List[Any], target: T) -> bool:
    return target in items
def check_item_in_dict(data: Dict[str, Any], key: str) -> bool:
    return key in data.keys()
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    target_value = 30
    sample_dict = {'a': 'apple', 'b': 'banana'}
    search_key = 'b'
    result_list = check_item_in_list(sample_list, target_value)
    result_dict = check_item_in_dict(sample_dict, search_key)
    print(f"Item in list: {result_list}")
    print("Key in dict:", result_dict)