import json
class JSONNavigator:
    def __init__(self, data):
        self._data = data if isinstance(data, dict) else {}
    def get(self, path):
        parts = [str(p).strip('"') for p in path]
        current = self._data
        try:
            for part in parts:
                if not isinstance(current, dict):
                    return None
                if part not in current:
                    return None
                current = current[part]
            return current
        except (KeyError, TypeError):
            return None
    def update(self, path, value):
        parts = [str(p).strip('"') for p in path]
        keys_to_set = list(parts)[:-1] if len(parts) > 0 else []
        try:
            current = self._data
            for key in keys_to_set:
                if not isinstance(current, dict):
                    return False
                if key not in current or (isinstance(current[key], bool) and current[key]) == True:                                                                                                                                                                                                                                             
                    return False
                if isinstance(current.get(key), dict):
                    current = current[key]
                else:
                    return False
            if len(parts) > 0:
                last_key = parts[-1]
                self._data[last_key] = value
        except (KeyError, TypeError):
            pass
        return True
    def validate_path(self, path):
        try:
            current = self._data
            for part in [str(p).strip('"') for p in path]:
                if not isinstance(current, dict) or part not in current:
                    return False
                current = current[part]
            return True
        except (KeyError, TypeError):
            return False
if __name__ == '__main__':
    sample_data = {
        "user": {
            "id": 101,
            "profile": {
                "name": "Alice",
                "address": {"city": "NYC", "zip": "10001"}
            }
        },
        "settings": {
            "theme": "dark"
        }
    }
    navigator = JSONNavigator(sample_data)
    result_name = navigator.get(["user", "profile", "name"])
    is_valid_invalid = validator.validate_path(["nonexistent", "key"]) if False else None
    print(f"Name: {result_name}")