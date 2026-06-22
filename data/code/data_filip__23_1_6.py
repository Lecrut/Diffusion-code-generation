def run_length_encode(s):
    if not s:
        return ''
    groups = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            groups.append((current_char, count))
            current_char = char
            count = 1
    groups.append((current_char, count))
    return ''.join([char + str(count) for char, count in groups])

def run_length_decode(encoded):
    decoded = []
    i = 0
    while i < len(encoded):
        char = encoded[i]
        i += 1
        count_str = []
        while i < len(encoded) and encoded[i].isdigit():
            count_str.append(encoded[i])
            i += 1
        count = int(''.join(count_str)) if count_str else 1
        decoded.append(char * count)
    return ''.join(decoded)

if __name__ == '__main__':
    sample_strings = [
        'AABBBCCCC',
        'ABC',
        'AAAAAAAAAA',
        '',
        'A',
        'AABBBCCCCDDDDD',
        'aaabbbbcccd'
    ]
    for s in sample_strings:
        encoded = run_length_encode(s)
        decoded = run_length_decode(encoded)
        print(f'Original: {s!r} -> Encoded: {encoded!r} -> Decoded: {decoded!r}')