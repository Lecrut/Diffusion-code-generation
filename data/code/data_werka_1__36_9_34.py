def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError('Input must be a string')
    char_map = {chr(i): chr(i) for i in range(256)}
    reversed_chars = []
    for char in s:
        reversed_chars.append(char_map[char])
    return ''.join(reversed_chars[::-1])
if __name__ == '__main__':
    sample_string = 'Alibaba Cloud AI'
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)