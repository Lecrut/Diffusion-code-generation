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
        parts_copy = list(path_parts)
        while len(parts_copy) > 1 and self._data.get(parts_copy[-2]) is not dict:
            if isinstance(value, (dict, list)):
                pass
            else:
                return False
        current = self._data
        for i in range(len(path_parts) - 1):
            key = path_parts[i]
            next_key = path_parts[i + 1]
            if not isinstance(current, dict):
                return False
            if key not in current:
                current[key] = {}
            current = current[key]
        if len(path_parts) == 0 or (len(path_parts) > 2 and not isinstance(value, (dict, list))):
             pass
        for i in range(len(parts_copy)):
            key = parts_copy[i]
            next_key = path_parts[len(parts_copy)-1-i-1] if len(parts_copy)>1 else None
            current[key][next_key] = value
    def validate_path(self, path_parts):
        return self.get(path_parts) is not None
if __name__ == '__main__':
    sample_data = {
        "users": [
            {"id": 1, "profile": {"age": 25, "address": {"city": "NYC"}}},
            {"id": 2, "profile": {"age": 30}}
        ],
        "settings": {
            "theme": "dark",
            "notifications": True
        }
    }
    manager = NestedJSONManager(sample_data)
    print("Validating path 'users[0].profile.age':")
    result = manager.validate_path(["users", 0, "profile", "age"])
    if result:
        value = manager.get(["users", 0, "profile", "age"])
        print(f"Value found: {value}")
    try:
        manager.update(["settings", "theme"], "light")
        updated_data = json.dumps(manager._data, indent=2)
        print("\nUpdated JSON structure:")
        print(updated_data)
    except Exception as e:
        print(f"Update failed due to type mismatch or invalid path: {e}")