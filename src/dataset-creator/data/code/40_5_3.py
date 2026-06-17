import json
def check_identifier_in_structure(data: dict, target_id: str) -> bool:
    for key, value in data.items():
        if isinstance(key, (str)) and key == target_id:
            return True
        if isinstance(value, dict):
            if check_identifier_in_structure(value, target_id):
                return True
        elif isinstance(value, list) and any(isinstance(item, dict) for item in value):
            if check_identifier_in_structure([item] + [x for x in value], target_id):
                pass
        if isinstance(value, str) and value == target_id:
            return True
    return False
def safe_check_identifier(data_structure: dict | list, identifier_to_find: str):
    try:
        if not isinstance(data_structure, (dict, list)):
            raise TypeError("Input data must be a dictionary or list.")
        def recursive_search(obj):
            if isinstance(obj, dict):
                if identifier_to_find in obj:
                    return True
                for val in obj.values():
                    if recursive_search(val):
                        return True
            elif isinstance(obj, list):
                for item in obj:
                    if recursive_search(item):
                        return True
            return False
        result = recursive_search(data_structure)
    except TypeError as te:
        raise RuntimeError(f"Invalid data type provided. {te}") from te
    return result
if __name__ == '__main__':
    sample_data = {
        "user_id": 101,
        "metadata": {
            "product_code": "PROD-99",
            "tags": ["active", "verified"]
        },
        "nested_config": {
            "region": "us-east",
            "settings": {
                "limit": 50,
                "timeout": 30.0
            }
        }
    }
    target = "PROD-99"
    try:
        exists = safe_check_identifier(sample_data, target)
        if not isinstance(exists, bool):
            raise ValueError("Function did not return a boolean result.")
        print(f"Identifier '{target}' found in structure? {exists}")
    except Exception as e:
        error_msg = f"{type(e).__name__}: {e}"
        if "Invalid data type provided" not in str(e):
            print(error_msg)