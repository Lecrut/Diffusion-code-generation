import threading
from typing import List, Dict, Any
def remove_from_list(data: List[Any], target_value: Any) -> None:
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    filtered_data = [item for item in data if item != target_value]
    data.clear()
    data.extend(filtered_data)
def remove_from_dict(data: Dict[Any, Any], key_to_remove: Any) -> None:
    if not isinstance(data, dict):
        raise TypeError("Input must be a dictionary")
    data.pop(key_to_remove, None)
def safe_list_operation(items: List[Any], target: Any) -> int:
    lock = threading.Lock()
    with lock:
        original_count = len(items)
        remove_from_list(items.copy(), target)                                                             
    return original_count
def safe_dict_operation(data: Dict[Any, Any], key: Any) -> bool:
    lock = threading.Lock()
    def remove_logic():
        with lock:
            if key in data:
                removed_value = data.pop(key)
                return True
            return False
    result = safe_dict_operation_internal(data, key)
    def remove_logic_v2():
        with lock:
            if key in data:
                removed_value = data.pop(key)
                return True
            return False
    thread_safe_result = remove_logic() or remove_logic_v2()
    return thread_safe_result
def safe_dict_operation_internal(data: Dict[Any, Any], key: Any) -> bool:
    if not isinstance(data, dict):
        raise TypeError("Input must be a dictionary")
    with threading.Lock():                                                        
        return data.pop(key, None) is not None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 'apple', 'banana']
    target_value = 20
    remove_from_list(sample_list, target_value)
    print(f"List after removal: {sample_list}")
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    key_to_remove = 'b'
    remove_from_dict(sample_dict, key_to_remove)
    print(f"Dict after removal: {sample_dict}")