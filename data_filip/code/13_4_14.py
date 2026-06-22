import re

def snake_to_camel(text: str) -> str:
    if '_' not in text:
        return text
    parts = text.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

def fast_snake_to_camel(text: str) -> str:
    return re.sub(r'_([a-zA-Z])', lambda m: m.group(1).upper(), text)

if __name__ == '__main__':
    test_cases = ['user_name', 'first_name_last_name', 'id', 'api_key', 'camel_case_string']
    for case in test_cases:
        print(fast_snake_to_camel(case))