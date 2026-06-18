import json
def safe_get(data: dict | list, *keys) -> any:
    current = data
    for key in keys:
        if isinstance(current, (dict, list)):
            try:
                index_or_key = int(key) if isinstance(key, str) and key.isdigit() else key
                if isinstance(current, dict):
                    value = current.get(index_or_key or key)
                elif isinstance(current, list):
                    length = len(current)
                    if not (0 <= index_or_key < length):
                        return None
                    value = current[index_or_key]
                else:
                    return None
            except Exception:
                return None
        else:
            return None
        current = value
    return current
if __name__ == '__main__':
    profile_data = {
        "user": [
            {"id": 1, "details": {"age": 25}},
            {"id": 2}
        ],
        "admin": True
    }
    try:
        user_id_1_age = safe_get(profile_data, "user", 0, "details", "age")
        print(f"User ID 1 Age: {user_id_1_age}")
        invalid_path = safe_get(profile_data, "nonexistent_key", "value")
        if invalid_path is None:
            print("Path not found or error occurred.")
    except Exception as e:
        print(f"Unexpected error during navigation: {e}")