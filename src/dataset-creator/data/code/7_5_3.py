import re
def sanitize_boolean_string(value: str) -> bool | None:
    if not isinstance(value, str):
        return value
    sanitized = value.strip().lower()
    valid_values = ['true', 'false']
    if sanitized in valid_values:
        return sanitized == 'true'
    normalized_map = {
        'y': True, 'n': False, 
        't': True, 'f': False,
        '1': True, '0': False,
        'yes': True, 'no': False,
        'true': True, 'false': False,
    }
    if sanitized in normalized_map:
        return normalized_map[sanitized]
    pattern = r'(?:^|[^a-z])([atfyn10]+)(?=[^\w]|$)'
    matches = re.findall(pattern, sanitized)
    if not matches:
        return None
    clean_word = re.sub(r'[^a-z]', '', sanitized)
    if len(clean_word) > 0:
        return sanitize_boolean_string(clean_word)
    return None
if __name__ == '__main__':
    test_cases = [
        "True", 
        "FALSE", 
        "tRuE", 
        "yes", 
        "no", 
        "1", 
        "0", 
        "  TRUE  ", 
        "invalid_input", 
        "",
        "yEs"
    ]
    results = []
    for case in test_cases:
        result = sanitize_boolean_string(case)
        if isinstance(result, bool):
            results.append(f"{case!r} -> {result}")
        else:
            results.append(f"{case!r} -> {type(result).__name__}: {result}")
    print("\n".join(results))