import json
from typing import Any, Dict, List, Optional
def check_item_existence(data: Any, target: Any) -> bool:
    def _recursive_check(current_data: Any, search_target: Any) -> bool:
        if isinstance(search_target, type(current_data)) and id(current_data) == id(search_target):
            return True
        if isinstance(current_data, (list, tuple)):
            for item in current_data:
                if _recursive_check(item, search_target):
                    return True
        elif isinstance(current_data, dict):
            for key, value in current_data.items():
                if str(key) == str(search_target):
                    return True
                if _recursive_check(value, search_target):
                    return True
        return False
    try:
        result = _recursive_check(data, target)
        return bool(result)
    except Exception:
        return False
def validate_json_structure(obj: Any) -> Optional[Dict[str, str]]:
    errors = []
    def _validate_serialization(item):
        try:
            json.dumps(item)
        except (TypeError, ValueError) as e:
            errors.append(f"Serialization failed at {type(item).__name__}: {str(e)}")
    if isinstance(obj, dict):
        for key in obj.keys():
            _validate_serialization(key)
            _validate_serialization(obj[key])
    elif isinstance(obj, (list, tuple)):
        for item in obj:
            _validate_serialization(item)
    return errors
if __name__ == '__main__':
    complex_data = {
        "user": {"id": 123, "details": ["active", True]},
        "products": [
            {"sku": "A001", "price": 9.99},
            {"sku": "B002", "price": 45.0}
        ],
        "metadata": {
            "tags": ["python", "json"],
            "version": (1, 0)
        }
    }
    target_item = "A001"
    exists = check_item_existence(complex_data, target_item)
    print(f"Item '{target_item}' found: {exists}")
    validation_errors = validate_json_structure(complex_data)
    if not validation_errors:
        print("JSON Structure Validation: PASSED")
    else:
        for error in validation_errors:
            print(f"Validation Error: {error}")