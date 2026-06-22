import re

_snake_to_camel_pattern = re.compile(r'_([a-zA-Z])')

def to_camel_case(snake_str: str) -> str:
    return _snake_to_camel_pattern.sub(lambda m: m.group(1).upper(), snake_str)

if __name__ == '__main__':
    sample_inputs = ["user_profile_data", "get_user_info", "max_retry_count", "simple"]
    for s in sample_inputs:
        print(to_camel_case(s))