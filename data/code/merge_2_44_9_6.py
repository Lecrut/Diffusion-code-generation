from typing import Any, Dict, List, Tuple, Union
def get_nested_value(data: Union[Dict[str, Any], List[Any]], path: Tuple[int, ...]) -> Any:
    current = data
    for index in path:
        if isinstance(current, dict):
            key_to_check = str(index)
            if key_to_check not in current:
                raise KeyError(f"Key '{key_to_check}' does not exist")
            current = current[key_to_check]
        elif isinstance(current, list):
            if index < 0 or index >= len(current):
                raise IndexError(f"Index {index} out of range for length {len(current)}")
            current = current[index]
        else:
            raise TypeError("Path must refer to a dictionary key or list index only.")
    return current
if __name__ == '__main__':
    sample_data = {
        "user": {
            "id": 101,
            "profile": {
                "name": "Alice",
                "tags": ["admin", "developer"]
            }
        },
        "products": [
            {"sku": "P001", "price": 9.99},
            {"sku": "P002", "price": 14.50}
        ]
    }
    test_paths = (
        ("user",),
        ("user", "profile"),
        ("products", 1, "sku"),
        ("nonexistent_key",)
    )
    for path in test_paths:
        try:
            result = get_nested_value(sample_data, path)
            print(f"Path {path}: {result}")
        except (KeyError, IndexError, TypeError) as e:
            print(f"Path {path} raised error: {e}")