import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def snake_to_camel_regex(snake_str):
    return re.sub(r'_([a-zA-Z])', lambda match: match.group(1).upper(), snake_str)

if __name__ == '__main__':
    test_cases = [
        "hello_world",
        "user_profile_data",
        "first_name",
        "last_name",
        "api_key",
        "response_time_ms",
        "is_valid_user",
        "max_retry_count",
        "empty_string",
        "a_b_c_d_e"
    ]
    
    for case in test_cases:
        result = snake_to_camel_regex(case)
        print(f"{case} -> {result}")