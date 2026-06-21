def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError('Input must be a string')
    reversed_chars = []
    for char in s:
        reversed_chars.append(char)
    reversed_chars.reverse()
    return ''.join(reversed_chars)
if __name__ == '__main__':
    SAMPLE_STRING1 = 'Hello, World!'
    SAMPLE_STRING2 = 'Alibaba Cloud'
    SAMPLE_STRING3 = 'Qwen, the AI assistant'
    try:
        print(reverse_string(SAMPLE_STRING1))
        print(reverse_string(SAMPLE_STRING2))
        print(reverse_string(SAMPLE_STRING3))
    except ValueError as e:
        print(e)