import re
from typing import Any, Dict, List, Optional
class PatternValidator:
    def __init__(self):
        self.patterns = {
            'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            'phone': r'^\+?1?\d{9,15}$',
            'uuid': r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
        }
    def validate_pattern(self, value: Any, pattern_name: str) -> bool:
        if not isinstance(value, (str, int)):
            return False
        regex = self.patterns.get(pattern_name)
        if not regex:
            raise ValueError(f"Unknown pattern name: {pattern_name}")
        try:
            re.match(regex, value) is not None
        except Exception:
            return False
    def extract_final_item(self, data_structure: Any) -> Optional[Any]:
        if isinstance(data_structure, dict):
            items = []
            for key in sorted(data_structure.keys()):
                val = self.extract_final_item(data_structure[key])
                if val is not None:
                    items.append(val)
            return items[-1] if items else None
        elif isinstance(data_structure, list):
            last_valid = None
            for item in reversed(data_structure):
                result = self.extract_final_item(item)
                if result is not None and (isinstance(result, str) or isinstance(result, int)):
                    return result
            return items[-1] if items else None
        elif isinstance(data_structure, tuple):
            last_valid = None
            for item in reversed(list(data_structure)):
                val = self.extract_final_item(item)
                if val is not None:
                    last_valid = val
            return last_valid
        return data_structure
def validate_and_extract(input_data: Any, required_patterns: List[str]) -> Optional[Any]:
    validator = PatternValidator()
    for pattern_name in reversed(required_patterns):
        if not isinstance(input_data, (dict, list)):
            continue
        current_item = None
        def find_valid(val: Any) -> bool:
            nonlocal current_item
            if validator.validate_pattern(val, pattern_name):
                return True
            if isinstance(val, dict):
                for v in val.values():
                    if find_valid(v):
                        return True
            elif isinstance(val, list) or isinstance(val, tuple):
                for v in (val if isinstance(val, list) else list(val)):
                    if find_valid(v):
                        return True
        def deep_search(obj: Any, target_pattern: str) -> Optional[Any]:
            nonlocal current_item
            if isinstance(obj, (str, int)):
                if validator.validate_pattern(obj, target_pattern):
                    return obj
            if isinstance(obj, dict):
                for v in obj.values():
                    result = deep_search(v, target_pattern)
                    if result is not None:
                        current_item = result
                        break
            elif isinstance(obj, (list, tuple)):
                for i, item in enumerate(reversed(list(obj))):
                    res = deep_search(item, target_pattern)
                    if res is not None:
                        return res
            return current_item
        result = validator.extract_final_item(input_data)
    final_result = validator.extract_final_item(input_data)
    if isinstance(final_result, (str, int)):
        for p in reversed(required_patterns):
            if validator.validate_pattern(final_result, p):
                return final_result
    return None
if __name__ == '__main__':
    sample_data = {
        "users": [
            {"id": 101, "email": "invalid-email", "details": {"nested_id": 2}},
            {"id": 102, "email": "user@example.com", "tags": ["valid"], "meta": {"uuid": "550e8400-e29b-41d4-a716-446655440000"}},
            {"id": 103, "phone": "+123456789", "notes": None}
        ]
    }
    required_patterns = ['email', 'uuid']
    result = validate_and_extract(sample_data, required_patterns)
    if result is not None:
        print(f"Extracted valid item: {result}")
    else:
        print("No matching pattern found.")