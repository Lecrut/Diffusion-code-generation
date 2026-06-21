import re

def snake_to_camel(identifier):
    if not identifier:
        return identifier
    if '_' not in identifier:
        return identifier[0].lower() + identifier[1:] if identifier else identifier
    parts = re.split(r'_+', identifier.strip('_'))
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    samples = [
        "hello_world",
        "foo_bar_baz",
        "alreadyCamel",
        "single",
        "__leading__trailing__",
        "multiple___underscores",
        "a_b_c_d_e",
        "",
        "_",
        "___"
    ]
    for sample in samples:
        print(snake_to_camel(sample))