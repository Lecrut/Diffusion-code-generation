def run_length_encode(s):
    if not s:
        return ''
    encoded = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(f"{count}{current_char}")
            else:
                encoded.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        encoded.append(f"{count}{current_char}")
    else:
        encoded.append(current_char)
    return ''.join(encoded)

def run_length_decode(s):
    decoded = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            count = 0
            while i < len(s) and s[i].isdigit():
                count = count * 10 + int(s[i])
                i += 1
            char = s[i]
            decoded.append(char * count)
            i += 1
        else:
            decoded.append(s[i])
            i += 1
    return ''.join(decoded)

if __name__ == '__main__':
    samples = [
        '',
        'a',
        'aaa',
        'aabbcc',
        'aaabbcddda',
        'xyz',
        '111222333',
        'hello world',
        '   ',
        'aAaA'
    ]
    for sample in samples:
        encoded = run_length_encode(sample)
        decoded = run_length_decode(encoded)
        print(f"Original: '{sample}'")
        print(f"Encoded:  '{encoded}'")
        print(f"Decoded:  '{decoded}'")
        print(f"Match:    {sample == decoded}")
        print()