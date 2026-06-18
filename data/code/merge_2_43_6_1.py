from typing import Any, List, Optional
def remove_targeted_items(data: Any) -> Any:
    if isinstance(data, dict):
        return {k: v for k, v in data.items() if "target" not in str(v).lower()}
    elif isinstance(data, list):
        filtered_list = []
        for item in data:
            item_str = str(item)
            if "remove_me" not in item_str.lower():
                filtered_list.append(item)
        return filtered_list
    else:
        raise TypeError("Input must be a dictionary or a list.")
if __name__ == '__main__':
    sample_dict = {
        'key1': 'value with target',
        'key2': 'safe value',
        'key3': 'another remove_me item'
    }
    sample_list = [
        1, "remove_me", True, "keep this", None, "delete"
    ]
    result_dict = remove_targeted_items(sample_dict)
    result_list = remove_targeted_items(sample_list)
    print("Processed Dictionary:", result_dict)
    print("Processed List:", result_list)