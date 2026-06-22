def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    
    parts = snake_str.split('_')
    result_parts = []
    
    for part in parts:
        if part:
            result_parts.append(part.capitalize())
        else:
            result_parts.append('')
    
    if snake_str.startswith('_'):
        return ''.join(result_parts)
    
    first = result_parts[0].lower() if result_parts else ''
    rest = ''.join(result_parts[1:])
    
    return first + rest

if __name__ == '__main__':
    test_cases = [
        "hello_world",
        "snake_case_string",
        "leading_underscore_example",
        "__double_underscore",
        "trailing_",
        "multiple___underscores",
        "alreadyCamel",
        "",
        "single",
        "_private_variable",
        "get_http_response_code"
    ]
    
    for test in test_cases:
        print(snake_to_camel(test))