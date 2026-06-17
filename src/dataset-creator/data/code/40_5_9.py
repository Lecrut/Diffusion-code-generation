import json
def check_identifier_existence(data_structure: dict, target_id: str) -> bool:
    try:
        for key in data_structure.keys():
            value = data_structure[key]
            if isinstance(key, str):
                if key == target_id:
                    return True
            elif isinstance(value, dict):
                if check_identifier_existence(value, target_id):
                    return True
            elif isinstance(value, list) and len(value) > 0 and isinstance(value[0], dict):
                for item in value:
                    if isinstance(item, dict) and check_identifier_existence(item, target_id):
                        return True
        return False
    except Exception as e:
        raise RuntimeError(f"Error during identifier search: {str(e)}")
if __name__ == '__main__':
    sample_data = {
        "user": {"id": 101},
        "profile": {
            "username": "john_doe",
            "tags": ["admin", "verified"]
        },
        "settings": {
            "theme": "dark"
        }
    }
    target = "user"
    try:
        exists = check_identifier_existence(sample_data, target)
        if exists:
            print(f"The identifier '{target}' was found.")
        else:
            print(f"The identifier '{target}' was not found.")
    except RuntimeError as error:
        print(error)