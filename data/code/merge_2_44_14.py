import json
from typing import Any, Dict, List, Optional
class SafeNestAccess:
    def __init__(self, data: Any):
        self._data = data
    def get(self, path: List[Any]) -> Optional[Any]:
        try:
            current = self._data
            for key in path:
                if isinstance(current, dict) and key in current:
                    current = current[key]
                elif isinstance(current, list):
                    idx = int(key)
                    if 0 <= idx < len(current):
                        current = current[idx]
                    else:
                        return None
                else:
                    raise KeyError(f"Unsupported type for key {key} at path segment")
            return current
        except Exception as e:
            print(f"Error accessing path {path}: {e}")
            return None
    def set(self, path: List[Any], value: Any) -> bool:
        try:
            current = self._data
            for key in path[:-1]:
                if isinstance(current, dict):
                    if key not in current:
                        current[key] = {}
                    elif not isinstance(current[key], list) and isinstance(key, int):
                        raise KeyError(f"Cannot set index on non-list")
                    else:
                        current = current[key]
                elif isinstance(current, list):
                    idx = int(key)
                    if 0 <= idx < len(current):
                        current[idx] = {}
                    else:
                        return False
                    current = current[idx]
            final_key = path[-1]
            if isinstance(final_key, str):
                if not isinstance(current, dict):
                    raise KeyError(f"Cannot set string key on non-dict")
                elif final_key in current and isinstance(current[final_key], list) and isinstance(final_key, int):
                    raise KeyError(f"Index access expected for integer keys")
            else:
                idx = int(final_key)
                if not isinstance(current, list):
                    raise KeyError(f"Cannot set index on non-list")
                elif 0 <= idx < len(current):
                    current[idx] = {}
                else:
                    return False
            setattr(self._data, final_key, value)
            return True
        except Exception as e:
            print(f"Error setting path {path}: {e}")
            return False
def create_sample_data() -> Dict[str, Any]:
    sample = {
        "users": [
            {"id": 1, "name": "Alice", "settings": {"theme": "dark"}},
            {"id": 2, "name": "Bob", "settings": {"notifications": True}},
            {"id": 3, "name": "Charlie"},
        ],
        "products": {
            "electronics": [
                {"sku": "L01", "price": 99.99},
                {"sku": "L02", "price": 45.50}
            ]
        }
    }
    return sample
if __name__ == '__main__':
    data = create_sample_data()
    access = SafeNestAccess(data)
    paths_to_check = [
        ["users", 1, "settings"],
        ["products", "electronics", 0],
        ["nonexistent_key"],
        ["users", 99]
    ]
    results: List[Optional[Any]] = []
    for path in paths_to_check:
        val = access.get(path)
        if isinstance(val, dict):
            print(f"Path {path} -> Dict found")
            nested_val = access.set(["users", 0], {"new_field": "value"})
            results.append(nested_val)
    final_data = json.dumps(access._data, indent=2)
    print("Final JSON structure:")
    print(final_data)