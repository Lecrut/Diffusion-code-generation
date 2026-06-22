import re

def snake_to_camel(text: str) -> str:
    if not text:
        return text
    parts = re.split(r'_+', text)
    if not parts:
        return text
    result = parts[0]
    for part in parts[1:]:
        if part:
            result += part.capitalize()
    return result

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('snake_case_converter'))
    print(snake_to_camel('alreadyCamelCase'))
    print(snake_to_camel('multiple___underscores___here'))
    print(snake_to_camel('leading_underscore_value'))