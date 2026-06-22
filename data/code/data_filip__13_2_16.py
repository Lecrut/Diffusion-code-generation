import re

def snake_to_camel(text: str) -> str:
    if not text:
        return text
    
    is_leading_underscore = text.startswith('_')
    
    if is_leading_underscore:
        work_text = text[1:]
    else:
        work_text = text
    
    if not work_text:
        if is_leading_underscore:
            return '_'
        return ''
    
    parts = work_text.split('_')
    non_empty_parts = [p for p in parts if p]
    
    if not non_empty_parts:
        if is_leading_underscore:
            return '_'
        return ''
    
    if len(non_empty_parts) == 1:
        result = non_empty_parts[0]
    else:
        first_part = non_empty_parts[0].lower()
        rest_parts = [p.capitalize() for p in non_empty_parts[1:]]
        result = first_part + ''.join(rest_parts)
    
    if is_leading_underscore:
        result = '_' + result
    
    return result

if __name__ == '__main__':
    test_cases = [
        "hello_world",
        "hello__world",
        "_hello_world",
        "___hello_world",
        "alreadyCamel",
        "no_underscores",
        "_",
        "a_b_c",
        "",
        "get_HTTP_response_code"
    ]
    
    for case in test_cases:
        print(f"{case!r} -> {snake_to_camel(case)!r}")