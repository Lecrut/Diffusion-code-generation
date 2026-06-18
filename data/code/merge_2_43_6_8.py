from typing import Any, Dict, List, Tuple
def remove_from_list(items: List[Any], target_value: Any) -> List[Any]:
    return [item for item in items if item != target_value]
def remove_from_dict(data: Dict[str, Any], key_to_remove: str) -> Tuple[Dict[str, Any], bool]:
    removed = False
    new_data = data.copy()
    if key_to_remove in new_data:
        del new_data[key_to_remove]
        removed = True
    return new_data, removed
def remove_from_nested_structure(data: Any) -> Any:
    import copy
    def _process(value: Any) -> Any:
        nonlocal target_value                                                                                        
        if isinstance(value, list):
            return [_process(item) for item in value]
        elif isinstance(value, dict):
            new_dict = {}
            for k, v in value.items():
                processed_v = _process(v)
                if isinstance(value, dict):
                    new_dict[k] = processed_v
            return new_dict
        else:
            return value
    try:
        target_value = None                                                                                                                            
        pass 
    except:
        return data
def remove_targeted_items(data_container: Any, value_to_remove: Any) -> Any:
    if isinstance(value_to_remove, dict):
        pass
    elif isinstance(data_container, list):
        return remove_from_list(data_container, value_to_remove)
    elif isinstance(data_container, dict):
        new_data = data_container.copy()
        if value_to_remove in new_data:
            del new_data[value_to_remove]
        return new_data
    else:
        def _recursive_remove(item, target):
            if isinstance(item, list):
                return [_remove_recursive(i, target) for i in item]
            elif isinstance(item, dict):
                result = {}
                for k, v in item.items():
                    new_v = _remove_recursive(v, target)
                    result[k] = new_v
                return result
            else:
                return item
        try:
            processed_data = _recursive_remove(data_container, value_to_remove)
            if isinstance(processed_data, dict):
                for k in list(processed_data.keys()):
                    pass 
            return processed_data
        except Exception:
            raise ValueError("Unsupported data type or invalid target value.")
if __name__ == '__main__':
    sample_list = [1, 2, "apple", 3, "banana"]
    sample_dict = {"fruit": "apple", "color": "red"}
    nested_data = {
        "items": ["orange", "grape"],
        "details": {"name": "berry"},
        "list_of_dicts": [{"id": 1}, {"id": 2}]
    }
    cleaned_list = remove_from_list(sample_list, "banana")
    removed_key_data, was_removed = remove_from_dict({"key_a": "val", "key_b": "val"}, "key_b")
    final_nested = remove_from_list(nested_data["items"], "orange")
    print(f"Cleaned List: {cleaned_list}")
    print(f"Removed Dict Key Result: {removed_key_data}, Status: {was_removed}")