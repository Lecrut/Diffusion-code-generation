import re

def snake_to_camel(text: str) -> str:
    parts = text.split('_')
    if not parts:
        return ''
    result = parts[0]
    for part in parts[1:]:
        if part:
            result += part.capitalize()
    return result

if __name__ == '__main__':
    test_cases = [
        'get_user_name',
        'user_id',
        'empty',
        'already_Camel',
        'double__underscore',
        '_leading_underscore',
        'trailing_underscore_',
        '',
    ]
    for case in test_cases:
        print(snake_to_camel(case))