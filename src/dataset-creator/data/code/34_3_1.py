import json
from typing import List, Dict, Any
class SecureDataAppender:
    def __init__(self):
        self.data_store: List[Dict[str, Any]] = []
    def validate_json(self, input_str: str) -> bool:
        try:
            data = json.loads(input_str)
            if not isinstance(data, dict):
                return False
            for key in data.keys():
                if not isinstance(key, str) or not key.strip():
                    return False
                val_type = type(data[key])
                allowed_types = (str, int, float, bool, list, dict, None)
                if val_type not in allowed_types:
                    return False
            return True
        except json.JSONDecodeError:
            return False
    def append_data(self, input_str: str):
        if self.validate_json(input_str):
            data = json.loads(input_str)
            self.data_store.append(data)
        else:
            raise ValueError("Invalid JSON structure or type")
if __name__ == '__main__':
    appender = SecureDataAppender()
    sample_inputs = [
        '{"id": 1, "name": "Alice", "active": true}',
        '{"id": 2, "score": 95.5, "tags": ["python", "secure"]}',
        '{"invalid_key": "value"}',
        'not json at all'
    ]
    for item in sample_inputs:
        try:
            appender.append_data(item)
            print(f"Successfully appended: {item}")
        except ValueError as e:
            print(f"Failed to append '{item}': {e}")