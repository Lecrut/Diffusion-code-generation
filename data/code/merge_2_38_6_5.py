import re
def create_secure_dictionary():
    def sanitize_value(value):
        if not isinstance(value, str):
            raise TypeError("Values must be strings.")
        safe_pattern = re.compile(r'^[a-zA-Z0-9\s\-_.]+$')
        sanitized = safe_pattern.sub('', value)
        return sanitized
    def validate_key(key):
        if not isinstance(key, str):
            raise TypeError("Keys must be strings.")
        key_sanitized = re.sub(r'[\x00-\x1f\x7f]', '', key)
        return key_sanitized
    secure_dict = {}
    sample_data = [
        ("user_1", "John Doe"),
        ("product_id", "Widget-2024"),
        ("category_name", "Electronics")
    ]
    for raw_key, raw_value in sample_data:
        validated_key = validate_key(raw_key)
        sanitized_value = sanitize_value(raw_value)
        if not (len(validated_key) > 0 and len(sanitized_value) > 0):
            continue
        secure_dict[validated_key] = sanitized_value
    return secure_dict
if __name__ == '__main__':
    my_dictionary = create_secure_dictionary()
    print(my_dictionary)