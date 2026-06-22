import re

def snake_to_camel(snake_str: str) -> str:
    if not snake_str:
        return snake_str
    
    leading_underscores = len(snake_str) - len(snake_str.lstrip('_'))
    trailing_underscores = len(snake_str) - len(snake_str.rstrip('_'))
    
    core_str = snake_str.strip('_')
    
    if not core_str:
        return snake_str
    
    parts = core_str.split('_')
    camel_parts = [parts[0]]
    
    for part in parts[1:]:
        if part:
            camel_parts.append(part.capitalize())
    
    camel_core = ''.join(camel_parts)
    return '_' * leading_underscores + camel_core + '_' * trailing_underscores

if __name__ == '__main__':
    test_cases = [
        "simple_example",
        "__leading_doubled",
        "trailing_doubled__",
        "__both__sides__",
        "consecutive__underscores",
        "___",
        "",
        "a",
        "a_b_c",
        "alreadyCamel",
        "single"
    ]
    
    for case in test_cases:
        result = snake_to_camel(case)
        print(result)