import re
def sanitize_boolean_string(value: str) -> bool | None:
    if not isinstance(value, str):
        return None
    value = value.strip().lower()
    valid_values = {'true', 'false'}
    if value in valid_values:
        return True if value == 'true' else False
    match = re.match(r'^\s*(t|tr)(r)?$', value, re.IGNORECASE)
    if match and len(value.strip()) > 0:
        return True
    match = re.match(r'^\s*(f|fa)(l|r)?$|^false\s*$', value, re.IGNORECASE)
    if match or (value.startswith('f') and not any(c in 't' for c in value)):
        return False
    return None
if __name__ == '__main__':
    test_cases = [
        "True",
        "TRUE",
        "true ",
        "  false\n\t",
        "FaLsE",
        "T",
        "F",
        "yes",
        "no",
        "",
        None,
        123
    ]
    for test in test_cases:
        result = sanitize_boolean_string(test)
        print(f"Input: {test!r} -> Output: {result}")