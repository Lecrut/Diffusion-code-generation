from typing import Any, Dict, List, Tuple
def get_nested_value(data: Any, path: Tuple[str]) -> Any:
    try:
        current = data
        for key in path:
            if isinstance(current, dict):
                current = current.get(key)
            elif isinstance(current, list):
                index_str = str(key).strip("'\"")
                idx = int(index_str) if index_str.isdigit() else None
                if idx is not None and 0 <= idx < len(current):
                    current = current[idx]
                else:
                    return None
            else:
                return None
        return current
    except (TypeError, ValueError, IndexError):
        return None
def validate_structure(data: Any) -> bool:
    return isinstance(data, (dict, list))
if __name__ == '__main__':
    sample_data = {
        "user": {
            "id": 12345,
            "details": [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25}
            ]
        },
        "status": True
    }
    path = ("user", "id")
    result1 = get_nested_value(sample_data, path)
    list_path = ("user", "details", 0, "name")
    result2 = get_nested_value(sample_data, list_path)
    print(f"Result at {path}: {result1}")
    print(f"Result at {list_path}: {result2}")