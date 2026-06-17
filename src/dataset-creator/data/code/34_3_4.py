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
                if not (isinstance(key, str) and len(key.strip()) > 0):
                    return False
            return True
        except json.JSONDecodeError:
            return False
    def append_data(self, text: str) -> None:
        if self.validate_json(text):
            data = json.loads(text)
            for key in list(data.keys()):
                del data[key]
            for k, v in data.items():
                if isinstance(v, (list, dict)):
                    try:
                        new_data = {k: [v]}
                        self.data.append(new_data)
                    except TypeError:
                        continue
        else:
            raise ValueError("Invalid JSON format")
if __name__ == '__main__':
    appender = SecureDataAppender()
    sample_input_1 = '{"id": 1, "value": [10, 20]}'
    sample_input_2 = 'invalid json'
    sample_input_3 = '{"key": true}'
    try:
        appender.append_data(sample_input_1)
        print("Data appended successfully")
    except ValueError as e:
        print(f"Error appending data: {e}")
    try:
        appender.append_data(sample_input_2)
    except ValueError as e:
        print(f"Expected error for invalid JSON: {e}")
    try:
        appender.append_data(sample_input_3)
        print("Data appended successfully")
    except ValueError as e:
        print(f"Error appending data: {e}")