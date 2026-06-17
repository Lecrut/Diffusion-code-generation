import json
def get_nested_value(data: dict, path: list) -> any:
    current = data
    for key in path:
        if isinstance(current, (dict, list)) and key in current:
            current = current[key]
        else:
            return None
    return current
def process_profile(profile_data):
    try:
        sample_structure = {
            "user": {
                "profile": {
                    "name": "Alice",
                    "details": {
                        "age": 30,
                        "location": {"city": "New York", "country": "USA"}
                    }
                },
                "settings": {
                    "notifications": True
                }
            }
        }
        path = ["user", "profile", "details"]
        if not isinstance(profile_data, dict):
            raise TypeError("Profile must be a dictionary")
        result = get_nested_value(sample_structure, path)
        return {
            "status": "success" if result else "missing_key_found",
            "data": result or {"message": "Key does not exist at specified depth"}
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
if __name__ == '__main__':
    output = process_profile({})
    print(json.dumps(output, indent=2))