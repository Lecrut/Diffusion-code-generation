import re

def snake_to_camel(text):
    if not text:
        return text
    components = text.split('_')
    if len(components) == 1 and components[0] == text:
        return text
    if not text.startswith('_'):
        components[0] = components[0].lower()
    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(components))

def snake_to_camel_regex(text):
    if not text:
        return text
    if re.match(r'^[a-z][a-z0-9]*$', text):
        return text
    components = re.split(r'_+', text)
    components = [comp for comp in components if comp]
    if not components:
        return text
    if not text.startswith('_'):
        components[0] = components[0].lower()
    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(components))

if __name__ == '__main__':
    test_cases = [
        "hello_world",
        "user_name",
        "first_name_and_last_name",
        "id",
        "snake_case_identifier",
        "XML_parser",
        "my_var",
        "a",
        "_leading_underscore",
        "trailing_underscore_",
        "__double_underscore__",
        "UPPERCASE",
        "mixed_Case_example",
        "alreadyCamelCase",
        "multiple___underscores"
    ]
    results = []
    for case in test_cases:
        converted = snake_to_camel_regex(case)
        results.append(f"{case} -> {converted}")
    for line in results:
        print(line)