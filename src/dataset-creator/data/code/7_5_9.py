import re
def sanitize_boolean_string(value: str) -> bool | None:
    if not isinstance(value, str):
        return None
    value = value.strip().lower()
    valid_values = {'true', 'false'}
    if value in valid_values:
        return True if value == 'true' else False
    pattern = r'^[tT][rR]ue$|^f[FaA]lse$|^[yY][eE][sS]$|[nN][oO]$'
    if re.match(pattern, value):
        return True if any(c in value for c in 'tyes') else False
    return None
if __name__ == '__main__':
    test_cases = [
        "True",
        "FALSE",
        "Yes",
        "no",
        "  TRUE  ",
        "maybe",
        "",
        "1",
        "0"
    ]
    for case in test_cases:
        result = sanitize_boolean_string(case)
        print(f"'{case}' -> {result}")