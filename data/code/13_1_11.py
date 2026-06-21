import re

def snake_to_camel(s):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), s)

if __name__ == '__main__':
    samples = ["hello_world", "foo_bar_baz", "alreadyCamel", "single_word", "__leading", "trailing__", "a_b_c"]
    for sample in samples:
        print(snake_to_camel(sample))