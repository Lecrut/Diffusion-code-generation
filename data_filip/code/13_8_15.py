def snake_to_camel(s: str) -> str:
    parts = s.split('_')
    if not parts:
        return ''
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    samples = ['hello_world', 'one_two_three', 'already_camel', 'snake_case', 'a_b', 'single', '_leading', 'trailing_', 'multiple___underscores']
    for sample in samples:
        print(f'{sample} -> {snake_to_camel(sample)}')