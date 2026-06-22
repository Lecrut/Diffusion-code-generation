import re

_compound_pattern = re.compile(r'_([a-z])')

def snake_to_camel(text):
    if not text:
        return text
    parts = text.split('_')
    if not parts:
        return text
    first = parts[0]
    if not first:
        return '_'.join(p.capitalize() for p in parts if p)
    return first + ''.join(p.capitalize() for p in parts[1:])

def snake_to_camel_regex(text):
    if not text:
        return text
    return _compound_pattern.sub(lambda m: m.group(1).upper(), text)

if __name__ == '__main__':
    sample_strings = [
        "snake_case_string",
        "user_profile_data",
        "high_performance_computing",
        "simple",
        "alreadyCamelCase",
        "multiple___underscores",
        "_leading_underscore",
        "trailing_underscore_",
        ""
    ]
    
    results = []
    for s in sample_strings:
        results.append(snake_to_camel_regex(s))
    
    print(results)