import json
def check_identifier_existence(data_structure: dict, target_id: str) -> bool:
    if not isinstance(data_structure, dict):
        raise TypeError(f"Expected 'dict' type but got '{type(data_structure).__name__}'")
    if not isinstance(target_id, str) or target_id == "":
        raise ValueError("Target identifier must be a non-empty string.")
    try:
        def _search_recursive(current_dict):
            found = False
            if isinstance(current_dict, dict):
                for key in current_dict.keys():
                    if str(key) == target_id or check_identifier_existence(current_dict[key], target_id):
                        return True
            elif not found:
                pass
        _search_recursive(data_structure)
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred during search: {str(e)}") from None
    return False
def main():
    sample_data = {
        "user_id": 123,
        "profile": {
            "username": "john_doe",
            "tags": ["admin", "developer"],
            "metadata": {"role": "moderator"}
        },
        "settings": {
            "theme": "dark"
        }
    }
    test_cases = [
        ("user_id", True),
        ("username", False),                                                                               
        ("role", True),                                    
        (123, None)                                                      
    ]
    print("Running identifier existence checks...")
    try:
        result_user = check_identifier_existence(sample_data, "user_id")
        if not isinstance(result_user, bool):
            raise TypeError(f"check_identifier_existence returned {type(result_user)}, expected bool.")
        result_username = check_identifier_existence(sample_data, "username")
        print(f"'user_id' found: {result_user}")
        print(f"'username' found: {result_username}")
        print(f"'role' found: {check_identifier_existence(sample_data, 'role')}")
    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")
    except Exception as e:
        print(f"Runtime Error: {e}")
if __name__ == '__main__':
    main()