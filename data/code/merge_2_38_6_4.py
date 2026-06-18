import re
def sanitize_string(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', s)
    return sanitized
def create_secure_dictionary(keys: list, values: dict) -> dict:
    if not isinstance(keys, list):
        raise TypeError("Keys must be provided as a list.")
    if not isinstance(values, dict):
        raise TypeError("Values must be provided as a dictionary.")
    secure_dict = {}
    for key in keys:
        if not isinstance(key, str):
            raise ValueError(f"Key '{key}' is not a string.")
        safe_key = sanitize_string(key)
        if value := values.get(safe_key):
            try:
                sanitized_value = json.loads(value) if isinstance(value, str) else value
                secure_dict[safe_key] = sanitized_value
            except (json.JSONDecodeError, TypeError):
                raise ValueError(f"Invalid value for key '{safe_key}'.")
    return secure_dict
import json
if __name__ == '__main__':
    sample_keys = ["user1", "pass@word!", "admin"]
    sample_values = {
        "user1": '{"id": 123, "role": "guest"}',
        "pass@word!": 'normal_value',
        "admin": '[{"name":"Alice"},{"name":"Bob"}]'
    }
    try:
        result_dict = create_secure_dictionary(sample_keys, sample_values)
        print(result_dict)
    except Exception as e:
        print(f"Error occurred during dictionary creation: {e}")