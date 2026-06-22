def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    if not parts:
        return ''
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    samples = ['hello_world', 'snake_case_to_camel_case', 'alreadyCamel', 'single', 'with__double__underscores']
    for sample in samples:
        print(snake_to_camel(sample))