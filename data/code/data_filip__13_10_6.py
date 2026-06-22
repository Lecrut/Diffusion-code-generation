import re

def snake_to_camel(snake_str):
    if not snake_str:
        return snake_str
    components = re.sub(r'_+', '_', snake_str).split('_')
    if not components:
        return snake_str
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    samples = [
        "hello_world",
        "snake_case_string",
        "multiple___underscores",
        "single",
        "",
        "alreadyCamel",
        "mixed_Snake_and_Camel"
    ]
    for sample in samples:
        print(f"'{sample}' -> '{snake_to_camel(sample)}'")