import re

def snake_to_camel(s):
    return re.sub(r'_([a-zA-Z])', lambda m: m.group(1).upper(), s)

if __name__ == '__main__':
    sample_values = [
        "hello_world",
        "foo_bar_baz",
        "alreadyCamel",
        "single_word",
        "_leading_underscore",
        "trailing_underscore_",
        "multiple___underscores",
        "with_numbers_123_456",
        "UPPER_CASE_WORDS",
        "mixed_Case_With_Numbers_123"
    ]
    for value in sample_values:
        print(snake_to_camel(value))