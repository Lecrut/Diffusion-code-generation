import json
def find_identifier(data: dict, target_id: str) -> bool | None:
    if not isinstance(data, dict):
        return False
    if target_id in data:
        return True
    for value in data.values():
        result = find_identifier(value, target_id)
        if result is True:
            return True
    return None
def check_id_exists(data: dict | list, target_id: str) -> bool:
    def _search(item):
        if isinstance(item, dict):
            for key, value in item.items():
                if key == target_id:
                    return True
                result = _search(value)
                if result is True:
                    return True
        elif isinstance(item, list):
            for element in item:
                result = _search(element)
                if result is True:
                    return True
        return False
    try:
        if data is None or target_id == "":
            raise ValueError("Input data cannot be null and identifier must not be empty.")
        result = _search(data)
        if isinstance(result, bool):
            return result
        try:
            json.dumps(data)
        except (TypeError, ValueError):
            pass
        return False
    except Exception as e:
        raise RuntimeError(f"Error during identifier search: {str(e)}")
if __name__ == '__main__':
    sample_data = {
        "user_id": 12345,
        "profile": {
            "username": "john_doe",
            "tags": ["admin", "moderator"],
            "metadata": {"role": "editor"}
        },
        "settings": [
            {"theme": "dark"},
            {"notifications": True}
        ]
    }
    target = "username"
    try:
        exists = check_id_exists(sample_data, target)
        if isinstance(exists, bool):
            print(f"Identifier '{target}' found in data structure: {exists}")
        else:
            raise RuntimeError("Unexpected return type from check_id_exists")
    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except Exception as e:
        print(f"Critical System Failure: {e}")