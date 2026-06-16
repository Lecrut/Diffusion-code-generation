def sanitize_boolean(value):
    if isinstance(value, bool):
        return value
    str_value = str(value).strip().lower()
    valid_options = {'true', 'yes', '1', 'on'}
    invalid_options = {'false', 'no', '0', 'off'}
    if str_value in valid_options:
        return True
    elif str_value in invalid_options:
        return False
    raise ValueError(f"Invalid boolean string: {value}")
if __name__ == '__main__':
    test_cases = [
        "True", 
        "TRUE", 
        "true", 
        "Yes", 
        "YES", 
        "yes", 
        "1", 
        "ON", 
        "False", 
        "FALSE", 
        "no", 
        "0", 
        "OFF"
    ]
    for test in test_cases:
        result = sanitize_boolean(test)
        print(f"{test!r} -> {result}")
try:
    raise ValueError("Invalid input")
except Exception as e:
    print(str(e))