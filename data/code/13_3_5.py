import json
from typing import Any, Optional, Union

class NestedPathAccess:
    def __init__(self, data: Union[dict, list]):
        self.data = data

    def get(self, path: str) -> Optional[Any]:
        if not path:
            return self.data
        keys = path.split('.')
        current = self.data
        for key in keys:
            if isinstance(current, dict):
                if key in current:
                    current = current[key]
                else:
                    return None
            elif isinstance(current, list):
                if key.isdigit():
                    index = int(key)
                    if 0 <= index < len(current):
                        current = current[index]
                    else:
                        return None
                else:
                    return None
            else:
                return None
        return current

    def get_or_raise(self, path: str) -> Any:
        if not path:
            return self.data
        keys = path.split('.')
        current = self.data
        for key in keys:
            if isinstance(current, dict):
                if key in current:
                    current = current[key]
                else:
                    raise KeyError(f"Key '{key}' not found in path '{path}'")
            elif isinstance(current, list):
                if key.isdigit():
                    index = int(key)
                    if 0 <= index < len(current):
                        current = current[index]
                    else:
                        raise IndexError(f"Index {index} out of range at path '{path}'")
                else:
                    raise KeyError(f"Invalid list index '{key}' at path '{path}'")
            else:
                raise TypeError(f"Cannot navigate deeper from non-container type {type(current).__name__} at key '{key}'")
        return current

if __name__ == '__main__':
    sample_data = {
        "user": {
            "profile": {
                "name": "Alice",
                "settings": {
                    "theme": "dark",
                    "notifications": True
                }
            },
            "roles": ["admin", "editor"]
        },
        "system": {
            "version": "2.1.0",
            "features": {
                "analytics": True,
                "beta": False
            }
        }
    }
    accessor = NestedPathAccess(sample_data)
    print(accessor.get("user.profile.settings.theme"))
    print(accessor.get("user.roles.1"))
    print(accessor.get("system.features.nonexistent"))
    print(accessor.get_or_raise("system.version"))