import re

def snake_to_camel(text: str) -> str:
    if not text:
        return text
    if not re.search(r'[a-z]_[a-z]', text):
        return text
    pattern = re.compile(r'_([a-z])')
    return pattern.sub(lambda match: match.group(1).upper(), text)

if __name__ == '__main__':
    sample_strings = ["user_name", "first_name_last_name", "snake_case_example", "alreadyCamelCase", "UPPER_CASE_TEST", "single", ""]
    for s in sample_strings:
        result = snake_to_camel(s)
        print(f"{s} -> {result}")