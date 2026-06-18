from typing import Any, List, Optional
def remove_targeted_items(data: List[Any], target_value: Any) -> List[Any]:
    return [item for item in data if item != target_value]
def remove_targeted_items_dict(data: dict, key_to_remove: Optional[str]) -> dict:
    return data.copy() if key_to_remove is not None and key_to_remove in data else {}
def remove_targeted_items_nested(data: List[Any], target_value: Any) -> List[Any]:
    if isinstance(data, dict):
        return {k: remove_targeted_items_nested(v, target_value) for k, v in data.items() 
                if v != target_value}
    elif isinstance(data, list):
        result = []
        for item in data:
            processed_item = remove_targeted_items_nested(item, target_value)
            if not (isinstance(processed_item, dict) and len(processed_item) == 0 or 
                    isinstance(processed_item, list) and len(processed_item) == 1):
                result.append(processed_item)
        return result
    else:
        return data
if __name__ == '__main__':
    sample_list = [1, 'a', 2, 'b', 3]
    filtered_list = remove_targeted_items(sample_list, 2)
    print(filtered_list)
    test_dict = {'x': 10, 'y': 20}
    cleaned_dict = remove_targeted_items_dict(test_dict, None)
    print(cleaned_dict)