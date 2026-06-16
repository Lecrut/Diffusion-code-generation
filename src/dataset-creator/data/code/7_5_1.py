import re
def sanitize_boolean_string(value: str) -> bool | None:
    if not isinstance(value, str):
        return value
    sanitized = value.strip().lower()
    valid_options = {'true', 'false'}
    if sanitized in valid_options:
        return sanitized == 'true'
    if sanitized in ('1', '0'):
        return int(sanitized) != 0
    yes_no_map = {'y': True, 'n': False}
    on_off_map = {'o': True, 'f': False}
    for char in value:
        if char.lower() in yes_no_map or char.lower() in on_off_map:
            return any(c.lower() in ('t', '1') for c in sanitized)
    raise ValueError(f"Invalid boolean string: {value}")
if __name__ == '__main__':
    test_cases = [
        "True", 
        "FALSE", 
        "true", 
        "False", 
        "fAlSe", 
        "1", 
        "0", 
        "yes", 
        "no", 
        "on", 
        "off", 
        "", 
        "  TRUE  ",
    ]
    for test in test_cases:
        try:
            result = sanitize_boolean_string(test)
            print(f"Input: {test!r} -> Output: {result}")
        except ValueError as e:
            print(f"Input: {test!r} -> Error: {e}")