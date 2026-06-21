import re

def snake_to_camel(snake_str: str) -> str:
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), snake_str)

if __name__ == '__main__':
    samples = [
        "hello_world",
        "foo_bar_baz",
        "alreadyCamel",
        "snake_case_example",
        "a",
        "_leading_underscore",
        "trailing_underscore_",
        "multiple__underscores"
    ]
    for sample in samples:
        print(snake_to_camel(sample))