from typing import Any, List, Dict
def check_list_item(item: Any, lst: List[Any]) -> bool:
    return item in lst
def check_dict_key(key: Any, dct: Dict[Any, Any]) -> bool:
    return key in dct
if __name__ == '__main__':
    sample_list = [5, 23, "apple", None]
    target_item = "apple"
    sample_dict: Dict[str, int] = {"id": 101, "code": 99}
    target_key = "code"
    list_result = check_list_item(target_item, sample_list)
    dict_result = check_dict_key(target_key, sample_dict)
    print(f"Item in list: {list_result}")
    print(f"Key in dictionary: {dict_result}")