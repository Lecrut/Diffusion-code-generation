import re

def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    components = re.split(r'_+', snake_str)
    if not components:
        return ""
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    samples = [
        "hello_world",
        "foo_bar_baz",
        "alreadyCamel",
        "snake_case_example",
        "a_b_c",
        "",
        "no_underscores",
        "multiple___underscores___here"
    ]
    for sample in samples:
        print(snake_to_camel(sample))