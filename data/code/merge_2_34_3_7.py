import json
class SecureDataAppender:
    def __init__(self):
        self.data = []
    def append(self, raw_input):
        try:
            parsed_data = json.loads(raw_input)
            if not isinstance(parsed_data, dict):
                raise ValueError("Input must be a JSON object.")
            for key in parsed_data.keys():
                if not isinstance(key, str) or len(key.strip()) == 0:
                    raise ValueError(f"Invalid key '{key}' found in input data.")
                val = parsed_data[key]
                if not isinstance(val, (str, int, float, bool)) and not isinstance(val, list):
                    raise TypeError(f"Unsupported value type for key '{key}': {type(val)}")
            self.data.append(parsed_data)
        except json.JSONDecodeError:
            print("JSON decode error.")
        except ValueError as ve:
            print(str(ve))
if __name__ == '__main__':
    appender = SecureDataAppender()
    sample_input_1 = '{"id": 1, "name": "Alice", "score": 95.0}'
    sample_input_2 = '{"email": "alice@example.com", "active": true}'
    invalid_input = '[1, 2, 3]'
    appender.append(sample_input_1)
    appender.append(sample_input_2)
    try:
        appender.append(invalid_input)
    except Exception as e:
        print(f"Error appending {invalid_input}: {e}")