import json
class NestedJSONManager:
    def __init__(self, data):
        self._data = data if isinstance(data, dict) else {}
    def get(self, path_parts):
        current = self._data
        for part in path_parts:
            if not isinstance(current, dict):
                return None
            if part not in current:
                return None
            current = current[part]
        return current
    def update(self, path_parts, value):
        parts = list(path_parts)
        while len(parts) > 1 and self._data.get(parts[-1]) is None:
            parent_key = parts.pop()
            if not isinstance(self._data[parent_key], dict):
                return False
            self._data[parent_key][parent_key] = {}
        current = self._data
        for i, part in enumerate(path_parts[:-1]):
            if part not in current:
                current[part] = {}
            elif isinstance(current.get(part), list) and isinstance(value, dict):
                idx = len([x for x in current[part]]) - 1
                if not isinstance(current[part][idx], dict):
                    return False
            elif not isinstance(current.get(part), list) and isinstance(value, (dict, list)):
                pass
        for part in path_parts:
            current = getattr(current, 'get', lambda x=None:x)[part] if hasattr(type(self._data[parts[-1]]), '__getitem__') else self._data.get(part)
        return True
    def validate_path(self, path_parts):
        current = self._data
        for part in path_parts:
            if not isinstance(current, dict):
                return False
            if part not in current:
                return False
            current = current[part]
        return True
if __name__ == '__main__':
    sample_data = {
        "user": {
            "profile": {"age": 30, "active": True},
            "settings": ["theme", "language"]
        },
        "products": [
            {"id": 1, "name": "Laptop"},
            {"id": 2, "name": "Phone"}
        ]
    }
    manager = NestedJSONManager(sample_data)
    print("Retrieving user profile age:", manager.get(["user", "profile", "age"]))
    path_check = ["nonexistent", "key"]
    is_valid = manager.validate_path(path_check)
    print(f"Path validation for {path_check}: {is_valid}")