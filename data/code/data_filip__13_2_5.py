import re

def snake_to_camel(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if not s:
        return s
    
    leading_underscores = len(s) - len(s.lstrip('_'))
    leading_underscores_str = s[:leading_underscores]
    stripped = s[leading_underscores:]
    
    parts = re.split(r'_+', stripped)
    parts = [p for p in parts if p]
    
    if not parts:
        return leading_underscores_str
    
    result_parts = [parts[0].lower()]
    for part in parts[1:]:
        if part:
            result_parts.append(part[0].upper() + part[1:].lower())
    
    camel_str = ''.join(result_parts)
    return leading_underscores_str + camel_str

if __name__ == '__main__':
    test_cases = [
        "hello_world",
        "leading_underscore",
        "__double_leading",
        "trailing_",
        "multiple___underscores",
        "_mixed_case_example_",
        "alreadyCamelCase",
        "ALL_CAPS",
        "a",
        "",
        "___",
        "___nested___example___here___"
    ]
    
    for case in test_cases:
        result = snake_to_camel(case)
        print(f"{case!r} -> {result!r}")