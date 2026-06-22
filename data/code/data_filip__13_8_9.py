def snake_to_camel(snake_str: str) -> str:
    if not snake_str:
        return ''
    parts = snake_str.split('_')
    if len(parts) == 1:
        return parts[0]
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample_inputs = [
        'hello_world',
        'one_two_three',
        'alreadyCamel',
        'single',
        'with_underscores_and_numbers_123',
        '_leading',
        'trailing_',
        '__double__',
        '',
        'a'
    ]
    for s in sample_inputs:
        print(f"'{s}' -> '{snake_to_camel(s)}'")