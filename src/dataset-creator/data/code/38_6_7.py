import re
def sanitize_string(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("Value must be a string.")
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', value)
    return sanitized
def create_secure_dictionary(**kwargs: dict) -> dict:
    if len(kwargs) == 0:
        raise ValueError("Dictionary cannot be empty.")
    validated_data = {}
    for k, v in kwargs.items():
        if not isinstance(k, str):
            raise TypeError(f"Key must be a string. Received type {type(k).__name__}.")
        safe_key = sanitize_string(k).strip()
        if len(safe_key) == 0:
            continue
        try:
            val_str = str(v)
            sanitized_val = sanitize_string(val_str)
            validated_data[safe_key] = sanitized_val
        except Exception as e:
            raise ValueError(f"Invalid value for key '{k}': {e}")
    return validated_data
if __name__ == '__main__':
    sample_dict = create_secure_dictionary(
        name="John Doe",
        age=25,
        city="New York City!",
        email="john@example.com"
    )
    print(sample_dict)