import json
class SecureDataAppender:
    def __init__(self):
        self.data = []
    def validate_json(self, raw_input) -> bool:
        try:
            data = json.loads(raw_input)
            if not isinstance(data, dict):
                return False
            for key in data.keys():
                if not isinstance(key, str):
                    return False
                if len(key.strip()) == 0:
                    return False
            for value in data.values():
                if not (isinstance(value, bool) or isinstance(value, int) or isinstance(value, float) or 
                        isinstance(value, str)):
                    return False
                if isinstance(value, str):
                    if len(value.strip()) == 0:
                        return False
            return True
        except json.JSONDecodeError:
            return False
    def append_data(self, raw_input) -> bool:
        validated = self.validate_json(raw_input)
        if not validated:
            print("Invalid JSON structure")
            return False
        try:
            data = json.loads(raw_input)
            for key in sorted(data.keys()):
                value = data[key]
                entry_data = {"key": str(key), "value": str(value)}
                self.data.append(entry_data)
            print("Data appended successfully")
            return True
        except Exception as e:
            print(f"Error processing JSON: {e}")
            return False
if __name__ == '__main__':
    appender = SecureDataAppender()
    sample_inputs = [
        '{"id": 1, "name": "Alice", "active": true}',
        '{"code": 42, "description": "System update"}',
        'invalid json here'
    ]
    for input_str in sample_inputs:
        result = appender.append_data(input_str)
        if not result:
            break