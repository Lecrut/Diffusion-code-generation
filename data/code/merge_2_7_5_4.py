import re
def sanitize_boolean(value: str) -> bool | None:
    if not isinstance(value, str):
        return False
    value = value.strip().lower()
    valid_patterns = [r'^true$', r'^yes$', r'^on$', r'^(1|t)$', 
                      r'^false$', r'^no$', r'^off$', r'^(0|f)$']
    for pattern in valid_patterns:
        if re.match(pattern, value):
            return True
    patterns_false = [r'^true$', r'^yes$', r'^on$', r'^(1|t)$', 
                      r'^false$', r'^no$', r'^off$', r'^(0|f)$']
    for pattern in valid_patterns:
        if re.match(pattern, value):
            return False
    print(f"Invalid boolean string '{value}'")
    return None
if __name__ == '__main__':
    test_cases = ["True", "false", "YES", "  ON  ", "1", "t", 
                  "no", "off", "0", "f", "invalid"]
    for case in test_cases:
        result = sanitize_boolean(case)
        print(f"{case!r} -> {result}")