import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def snake_to_camel_regex(snake_str):
    pattern = re.compile(r'_(\w)')
    return pattern.sub(lambda match: match.group(1).upper(), snake_str)

if __name__ == '__main__':
    test_cases = [
        'user_id',
        'first_name',
        'max_value',
        'http_response_code',
        'already_camelCase',
        'single'
    ]
    
    print("--- Testing snake_to_camel_regex ---")
    for case in test_cases:
        result = snake_to_camel_regex(case)
        print(f"Input: {case} -> Output: {result}")