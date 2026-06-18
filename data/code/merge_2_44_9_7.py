from typing import Any, Dict, List, Union
def get_nested_value(data: Dict[str, Any], path: List[Union[int, str]]) -> Any:
    current = data
    for key in path:
        if isinstance(key, int):
            try:
                index = key
                if not (0 <= index < len(current)):
                    raise IndexError(f"Index {index} out of range")
                current = current[index]
            except TypeError as e:
                return None
        elif isinstance(key, str):
            if key in current and isinstance(current[key], dict) or isinstance(current[key], list):
                current = current[key]
            else:
                raise KeyError(f"Key '{key}' not found")
        else:
            raise TypeError("Path must contain only integers (for lists) or strings (for dicts)")
    return current
if __name__ == '__main__':
    sample_data = {
        "user": {"id": 1, "details": ["Alice", "Bob"]},
        "config": {"theme": "dark"},
        "items": [10, 20, 30]
    }
    test_paths = [
        ["user", "details"],
        ["user", "id"],
        ["config", "theme"],
        ["items", 1],
        ["nonexistent"]
    ]
    for path in test_paths:
        try:
            result = get_nested_value(sample_data, path)
            print(f"Path {path}: {result}")
        except Exception as e:
            print(f"Error accessing path {path}: {e}")