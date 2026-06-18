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
def get_user_profile(data: dict) -> any:
    path = ["user", "profile"]
    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary.")
    try:
        return get_nested_value(data, path)
    except Exception as e:
        print(f"Error accessing profile information: {e}")
        return None
if __name__ == '__main__':
    sample_data = {
        "user": {
            "profile": {
                "id": 12345,
                "name": "Alice",
                "address": [
                    {"city": "New York"},
                    {"state": "NY"}
                ]
            }
        },
        "settings": {}
    }
    profile = get_user_profile(sample_data)
    if isinstance(profile, dict):
        print(f"Profile ID: {profile.get('id')}")
        print(f"Name: {profile.get('name')}")