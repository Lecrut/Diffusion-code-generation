import json
def get_nested_value(data: dict, path: list) -> any:
    current = data
    for key in path:
        if isinstance(current, (dict, list)) and key in current:
            try:
                current = current[key]
            except Exception:
                return None
        else:
            return None
    return current
def get_user_profile(data: dict) -> any:
    path = ["user", "profile"]
    if not isinstance(data, dict):
        print("Error: Input data is not a dictionary.")
        return None
    try:
        value = get_nested_value(data, path)
        if value is None or (isinstance(value, dict) and "name" in value):
            name = value.get("name")
            if isinstance(name, str):
                print(f"User found: {name}")
                return True
            else:
                print("Error: User profile 'name' is not a string.")
                return False
        else:
            print("Error: Could not locate user profile data.")
            return False
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return None
if __name__ == '__main__':
    sample_data = {
        "user": {
            "profile": {
                "id": 12345,
                "email": "test@example.com",
                "name": "Alice Johnson"
            }
        },
        "settings": {
            "theme": "dark"
        }
    }
    get_user_profile(sample_data)