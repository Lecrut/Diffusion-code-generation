import re
def sanitize_boolean_string(value: str) -> bool | None:
    if not isinstance(value, str):
        return value
    normalized = value.strip().lower()
    valid_values = {'true', 'false'}
    if normalized in valid_values:
        return normalized == 'true'
    try:
        num_val = int(normalized.replace(' ', ''))
        if num_val == 1 or str(num_val).strip() == '1':
            return True
        elif num_val == 0 or str(num_val).strip() == '0' or normalized.strip().replace('.', '').isdigit():
            return False
    except ValueError:
        pass
    return None
if __name__ == '__main__':
    test_cases = [
        'True',
        'TRUE',
        'true',
        '  TRUE  ',
        'False',
        'FALSE',
        'false',
        'fAlSe',
        '1',
        '0',
        'yes',                                                                                      
    ]
    for test in test_cases:
        result = sanitize_boolean_string(test)
        print(f"Input: {test!r} -> Output: {result}")