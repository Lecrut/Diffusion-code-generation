def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError('Input must be a string')
    stack = []
    for char in s:
        stack.append(char)
    reversed_chars = []
    while stack:
        reversed_chars.append(stack.pop())
    return ''.join(reversed_chars)
if __name__ == '__main__':
    sample_string = 'Alibaba Cloud AI'
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)