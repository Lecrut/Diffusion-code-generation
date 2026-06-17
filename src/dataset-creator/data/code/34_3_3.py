import json
class SecureDataAppender:
    def __init__(self):
        self.data = []
    def validate_json(self, text: str) -> bool:
        try:
            data = json.loads(text)
            if not isinstance(data, dict):
                return False
            for key in data.keys():
                if not isinstance(key, str) or len(key.strip()) == 0:
                    return False
                value = data[key]
                if not isinstance(value, (str, int, float, bool)) and not isinstance(value, list):
                    return False
                if isinstance(value, dict):
                    for k in value.keys():
                        if not isinstance(k, str) or len(k.strip()) == 0:
                            return False
            return True
        except json.JSONDecodeError:
            return False
    def append_data(self, text: str) -> bool:
        if self.validate_json(text):
            data = json.loads(text)
            for key in data.keys():
                value = data[key]
                entry = {key: value}
                self.data.append(entry)
            return True
        else:
            print("Invalid JSON structure")
            return False
if __name__ == '__main__':
    appender = SecureDataAppender()
    sample_input_1 = '{"username": "alice", "age": 30}'
    sample_input_2 = '{"email": "bob@example.com", "active": true, "scores": [95, 87]}'
    sample_input_3 = 'invalid json'
    appender.append_data(sample_input_1)
    appender.append_data(sample_input_2)
    result = appender.append_data(sample_input_3)
    print(f"Append success for valid inputs: {appender.validate_json(json.dumps(appender.data[0])) and appender.validate_json(json.dumps(appender.data[1]))}")
    print(f"Append failed for invalid input as expected: {not result}")