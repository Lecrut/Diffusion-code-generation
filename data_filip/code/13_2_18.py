import re

def snake_to_camel(text):
    if not text:
        return text
    leading_underscores = len(text) - len(text.lstrip('_'))
    trailing_underscores = len(text) - len(text.rstrip('_'))
    core = text[leading_underscores:len(text) - trailing_underscores if trailing_underscores else len(text)]
    if not core:
        return text
    parts = [part for part in core.split('_') if part]
    if not parts:
        return text
    result = parts[0].lower()
    for part in parts[1:]:
        if part:
            result += part.capitalize()
    return '_' * leading_underscores + result + '_' * trailing_underscores

if __name__ == '__main__':
    test_cases = [
        "snake_case_example",
        "__leading_underscore",
        "trailing_underscore__",
        "consecutive___underscores",
        "alreadyCamel",
        "a",
        "__",
        "",
        "mixed______CASE___test",
        "___start___middle___end___"
    ]
    for case in test_cases:
        print(snake_to_camel(case))