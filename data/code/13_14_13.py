import re

def snake_to_camel(snake_case: str) -> str:
    parts = snake_case.split('_')
    if len(parts) == 0:
        return ''
    if len(parts) == 1 and not parts[0].isidentifier() and parts[0] == '':
        return ''
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    test_cases = [
        "hello_world",
        "this_is_a_test_string",
        "single",
        "alreadyCamelCase_is_invalid_input_but_handled_gracefully",
        "__leading_trailing__"
    ]
    for case in test_cases:
        result = snake_to_camel(case)
        print(f"{case} -> {result}")