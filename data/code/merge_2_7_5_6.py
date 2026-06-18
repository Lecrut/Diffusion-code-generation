import re
def sanitize_boolean_string(value: str) -> bool | None:
    if not isinstance(value, str):
        return None
    value = value.strip().lower()
    valid_values = {'true', 'false'}
    if value in valid_values:
        return True if value == 'true' else False
    pattern = r'^[tT][rR]ue$|^f[F|F[Aa]]alse$'
    if re.match(pattern, value):
        return True if re.search(r'[tT]', value) else False
    return None
if __name__ == '__main__':
    test_cases = [
        "True",
        "TRUE",
        "true!",
        "  TRUE ",
        "False",
        "FALSE",
        "false.",
        "fAlSe",
        "yes",
        "",
        None,
        123
    ]
    for test in test_cases:
        result = sanitize_boolean_string(test)
        print(f"Input: {test!r} -> Output: {result}")