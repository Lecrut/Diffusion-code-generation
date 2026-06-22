def run_length_encode(s):
    if not s:
        return ''
    encoded = []
    count = 1
    current_char = s[0]
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(current_char)
            encoded.append(str(count))
            current_char = char
            count = 1
    encoded.append(current_char)
    encoded.append(str(count))
    return ''.join(encoded)

if __name__ == '__main__':
    sample_strings = [
        'AABBCC',
        'ABC',
        'AAAAABBBCCD',
        'A',
        '',
        'aabbccddeeff',
        'AAAAABBBBBCCCCC'
    ]
    for s in sample_strings:
        result = run_length_encode(s)
        print(result)