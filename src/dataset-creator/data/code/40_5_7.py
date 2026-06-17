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
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict) and check_identifier_existence(item, target_id):
                        return True
        return False
    except Exception as e:
        raise RuntimeError(f"Error during identifier search: {str(e)}")
if __name__ == '__main__':
    sample_data = {
        "user": 12345,
        "profile": {"id": "USR-001", "active": True},
        "settings": [
            {"theme": "dark"},
            {"notifications": False}
        ],
        "metadata": {
            "version": "1.0",
            "tags": ["alpha", "beta"]
        }
    }
    target = "USR-001"
    try:
        exists = check_identifier_existence(sample_data, target)
        if exists:
            print(f"Identifier '{target}' found.")
        else:
            print(f"Identifier '{target}' not found.")
    except RuntimeError as error:
        print(error)