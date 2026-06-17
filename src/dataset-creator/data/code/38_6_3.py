import re
def sanitize_string(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("Value must be a string.")
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', value)
    return sanitized
def create_secure_dictionary(keys: list, values: dict) -> dict:
    for key in keys:
        if not isinstance(key, str):
            raise TypeError(f"All keys must be strings. Got {type(key).__name__}.")
    safe_values = {}
    for k, v in values.items():
        sanitized_v = sanitize_string(str(v)) if not isinstance(v, str) else sanitize_string(v)
        safe_values[k] = sanitized_v
    return dict(zip(keys, safe_values.values()))
if __name__ == '__main__':
    sample_keys = ["user_name", "email_address", "full_name"]
    raw_data = {
        "user_name": "<script>alert('xss')</script>",
        "email_address": "test@example.com; evil@attacker.com",
        "full_name": "John \"Johnny\" Doe"
    }
    secure_dict = create_secure_dictionary(sample_keys, raw_data)
    print(secure_dict)