import re

def snake_to_camel(identifier: str) -> str:
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), identifier)

if __name__ == '__main__':
    samples = [
        'hello_world',
        'snake_case_identifier',
        'alreadyCamel',
        'multiple___underscores',
        'a_b_c',
        'single',
        'with_numbers_123_test',
        '_leading_underscore',
        'trailing_underscore_',
        'ALL_UPPER_CASE'
    ]
    for sample in samples:
        print(f"{sample} -> {snake_to_camel(sample)}")