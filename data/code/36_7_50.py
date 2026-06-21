def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError('Input must be a string')
    char_stack = []
    for char in s:
        char_stack.append(char)
    reversed_chars = []
    while char_stack:
        reversed_chars.append(char_stack.pop())
    return ''.join(reversed_chars)
if __name__ == '__main__':
    sample_string = 'Hello, 世界!'
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)