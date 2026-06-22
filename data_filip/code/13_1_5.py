import re

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def to_camel_case_regex(snake_str):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), snake_str)

if __name__ == '__main__':
    sample_identifiers = ['user_id', 'first_name', 'account_balance', 'is_active', 'max_retry_count']
    for identifier in sample_identifiers:
        result = to_camel_case_regex(identifier)
        print(f"{identifier} -> {result}")