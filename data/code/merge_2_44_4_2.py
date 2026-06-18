import json
def get_nested_value(data: dict, path: list) -> any:
    current = data
    for key in path:
        if isinstance(current, (dict, list)) and key in current:
            try:
                current = current[key]
            except TypeError:
                return None
        else:
            return None
    return current
def safe_get_profile(profile_data: dict) -> any:
    path_keys = ["user", "profile"]
    if not isinstance(profile_data, dict):
        raise ValueError("Profile data must be a dictionary")
    try:
        return get_nested_value(profile_data, path_keys)
    except Exception as e:
        print(f"Error accessing profile information: {e}")
        return None
if __name__ == '__main__':
    sample_profile = {
        "user": {
            "profile": {
                "id": 12345,
                "username": "johndoe",
                "email": "john@example.com"
            }
        },
        "settings": {}
    }
    result = safe_get_profile(sample_profile)
    if isinstance(result, dict):
        print(f"Profile ID: {result.get('id')}")
        print(f"Username: {result.get('username')}")