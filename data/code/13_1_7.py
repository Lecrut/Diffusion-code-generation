import re

def snake_to_camel(snake_str: str) -> str:
    if not snake_str:
        return ""
    
    parts = re.split(r'_+', snake_str)
    if not parts:
        return ""
    
    first_part = parts[0].lower()
    camel_case_parts = [first_part]
    
    for part in parts[1:]:
        if not part:
            continue
        camel_case_parts.append(part[0].upper() + part[1:].lower())
    
    return "".join(camel_case_parts)

if __name__ == '__main__':
    sample_snake_cases = [
        "user_profile_data",
        "max_retries",
        "http_request_timeout",
        "first_last_name",
        "i_am_snake",
        "single",
        "__leading_trailing__"
    ]
    
    for sample in sample_snake_cases:
        result = snake_to_camel(sample)
        print(result)