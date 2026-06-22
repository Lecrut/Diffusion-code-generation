import re

def snake_to_camel(snake_str: str) -> str:
    if not snake_str:
        return ""
    if '_' not in snake_str:
        return snake_str
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    test_cases = [
        "hello_world",
        "snake_case_to_camel_case",
        "single",
        "multiple___underscores",
        "",
        "alreadyCamelCase"
    ]
    for case in test_cases:
        result = snake_to_camel(case)
        print(f"{case} -> {result}")