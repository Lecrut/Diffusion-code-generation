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
                if not (isinstance(value, list) and all(isinstance(item, int) for item in value)):
                    return False
            return True
        except json.JSONDecodeError:
            return False
    def append(self, text: str):
        if self.validate_json(text):
            data = json.loads(text)
            self.data.append(data)
if __name__ == '__main__':
    appender = SecureDataAppender()
    sample_input_1 = '{"user": [1, 2], "age": [30]}'
    sample_input_2 = 'invalid'
    sample_input_3 = '{key: value}'
    if appender.validate_json(sample_input_1):
        appender.append(sample_input_1)
    try:
        appender.append(sample_input_2)
    except json.JSONDecodeError:
        pass
    if not appender.validate_json(sample_input_3):
        print("Invalid structure detected.")