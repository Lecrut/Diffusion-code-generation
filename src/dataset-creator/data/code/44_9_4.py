from typing import Any, Dict, List, Union
def get_nested_value(data: Union[Dict[str, Any], List[Any]], path: List[int]) -> Any:
    if not isinstance(path, list) or len(path) == 0:
        raise ValueError("Path must be a non-empty list of integers.")
    current = data
    for index in path:
        if not isinstance(current, (dict, list)):
            return None
        try:
            if isinstance(current, dict):
                key_to_check = str(index)
                if key_to_check not in current:
                    raise KeyError(f"Key '{key_to_check}' not found.")
                current = current[key_to_check]
            else:
                if index < 0 or index >= len(current):
                    raise IndexError("Index out of range.")
                current = current[index]
        except (KeyError, IndexError) as e:
            return None
    return current
if __name__ == '__main__':
    sample_data = {
        "user": {
            0: {"id": 123, "details": ["active", True]},
            1: {"status": "verified"}
        },
        "products": [
            {"sku": "A-001"},
            {"sku": "B-002"}
        ]
    }
    test_paths = [
        ["user", 0, "details"],                                                                                                                                                                                                                                                                                                                                                           
        [0],                   
        ["user", 1]                   
    ]
    results = []
    for p in test_paths:
        try:
            val = get_nested_value(sample_data, p)
            if isinstance(val, dict):
                print(f"Path {p}: Dict found. Keys: {list(val.keys())}")
            else:
                print(f"Path {p}: Value is {val} (Type: {type(val).__name__})")
        except Exception as e:
            print(f"Error accessing path {p}: {e}")
    result_list = get_nested_value(sample_data, ["products", 0])
    if isinstance(result_list, dict):
        print(f"\nPath ['products', 0]: Dict found. Keys: {list(result_list.keys())}")