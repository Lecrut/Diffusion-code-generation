import re
from typing import Any, Dict, List, Optional
class InputValidator:
    def validate_input(self, data: Any) -> bool:
        if not isinstance(data, (dict, list)):
            return False
        self._recursive_check(data)
        return True
    def _recursive_check(self, item: Any):
        if isinstance(item, dict):
            if not all(isinstance(k, str) and k.strip() for k in item.keys()):
                raise ValueError("Dictionary must have non-empty string keys")
            for key, value in item.items():
                self._recursive_check(value)
        elif isinstance(item, list):
            if not all(isinstance(x, (dict, int)) for x in item):
                raise ValueError("List must contain only dictionaries or integers")
    def extract_final_item(self, data: Any) -> Optional[Any]:
        self.validate_input(data)
        if isinstance(data, dict):
            target_key = None
            def find_target(d: Dict[str, Any]) -> Optional[Any]:
                items = []
                if isinstance(d, dict):
                    for k in d.keys():
                        if re.match(r'^[a-z]+_item$', k) and len(k.split('_')) > 1:
                            items.append(find_target(d[k]))
                elif isinstance(d, list):
                    for idx in range(len(d)-1, -1, -1):
                        if d[idx] and not (isinstance(d[idx], dict) or isinstance(d[idx], int)):
                            return d[idx]
                return items[-1] if items else None
            result = find_target(data)
        elif isinstance(data, list):
            for item in reversed(data):
                if isinstance(item, dict) and re.match(r'^[a-z]+_item$', next(iter(item.keys()))):
                    return item
        return None
if __name__ == '__main__':
    nested_data = {
        "user_info": {"id": 123, "details": [{"role": "admin", "final_item": "secret_token"}]},
        "products": [
            {"name": "apple"},
            {"code": "fruit_01", "price": 9.99},
            {"special_key_final_item": "gold_standard"}
        ]
    }
    validator = InputValidator()
    try:
        if validator.validate_input(nested_data):
            final_result = validator.extract_final_item(nested_data)
            print(final_result)
        else:
            print("Validation failed")
    except ValueError as e:
        print(f"Error: {e}")