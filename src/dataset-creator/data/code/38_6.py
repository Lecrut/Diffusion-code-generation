import re
def sanitize_value(value):
    return re.sub(r'[<>`|&;(){}]', '', str(value))
def create_secure_dictionary(keys_data, values_data):
    secure_dict = {}
    if len(keys_data) != len(values_data):
        raise ValueError("Keys and values must have the same length.")
    for key_str, value in zip(keys_data, values_data):
        if not isinstance(key_str, str):
            raise TypeError(f"Key must be a string. Got {type(key_str).__name__}.")
        sanitized_value = sanitize_value(value)
        secure_dict[key_str] = sanitized_value
    return secure_dict
if __name__ == '__main__':
    keys_data = ["user_name", "email_address", "full_name"]
    values_data = [12345, "<script>alert('xss')</script>", 67890]
    result = create_secure_dictionary(keys_data, values_data)
    print(result)