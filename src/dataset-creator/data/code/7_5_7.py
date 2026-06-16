import re
def sanitize_boolean_string(s: str) -> bool | None:
    s = s.strip().lower()
    if not any(key in s for key in ['true', 'false']):
        return None
    try:
        return True if s == 'true' else False
    except ValueError:
        return None
if __name__ == '__main__':
    test_cases = [
        "True",
        "FALSE",
        "  TRUE ",
        "falsey value",
        "TRUEY",
        "",
        "maybe",
        "1",
        "0"
    ]
    for case in test_cases:
        result = sanitize_boolean_string(case)
        print(f"'{case}' -> {result}")