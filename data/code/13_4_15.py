import re

def snake_to_camel(snake_str: str) -> str:
    parts = snake_str.split('_')
    return parts[0] + ''.join(part.capitalize() for part in parts[1:])

if __name__ == '__main__':
    test_cases = [
        "hello_world",
        "user_profile_data",
        "single_word",
        "alreadyCamelCase",
        "deeply_nested_structure_name"
    ]
    for case in test_cases:
        result = snake_to_camel(case)
        print(result)