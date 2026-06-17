from typing import Any, Dict, List
def get_nested_value(data: Dict[str, Any], path: List[Any]) -> Any:
    if not data and len(path) == 0:
        return None
    current = data
    for key in path:
        if isinstance(current, dict):
            if key not in current:
                raise KeyError(f"Key {key} not found")
            current = current[key]
        elif isinstance(key, int):
            if isinstance(current, list) and 0 <= len(current) > key >= 0:
                current = current[key]
            else:
                raise IndexError("Index out of range or invalid type for path element")
        else:
            raise TypeError(f"Unsupported path element type: {type(key)}")
    return current
if __name__ == '__main__':
    sample_data = {
        "user": {"id": 1, "details": {"age": 30}},
        "products": [
            {"sku": "A", "price": 10.5},
            {"sku": "B", "price": 20.0}
        ],
        "config": {
            "theme": "dark"
        }
    }
    paths = [
        ["user", "details", "age"],
        ["products", 1, "price"],
        ["config", "theme"]
    ]
    for p in paths:
        try:
            val = get_nested_value(sample_data, p)
            print(f"Path {p}: {val}")
        except Exception as e:
            print(f"Error accessing path {p}: {e}")