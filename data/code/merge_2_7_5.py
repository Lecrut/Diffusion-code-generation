import re
def sanitize_boolean_string(value: str) -> bool | None:
    if not isinstance(value, str):
        return None
    normalized = value.strip().lower()
    valid_patterns = [r'^true$', r'^yes$', r'^on$', r'^1$']
    invalid_patterns = [r'^false$', r'^no$', r'^off$', r'^0$']
    if re.match(r'^(t|y|o|1)$', normalized):
        return True
    for pattern in valid_patterns:
        if re.match(pattern, normalized):
            return True
    for pattern in invalid_patterns:
        if re.match(pattern, normalized):
            return False
    return None
if __name__ == '__main__':
    test_cases = [
        "True",
        "TRUE",
        "true",
        "  TRUE  ",
        "Yes",
        "YES",
        "yes",
        "1",
        "FALSE",
        "false",
        "No",
        "0",
        "",
        "maybe",
        None,
    ]
    for case in test_cases:
        result = sanitize_boolean_string(case)
        print(f"Input: {case!r} -> Output: {result}")