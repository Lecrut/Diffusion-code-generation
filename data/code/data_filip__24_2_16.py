def rle_encode(data):
    if not data:
        return ''
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char and count < 9:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded.append(str(count) + current_char)
    return ''.join(encoded)

def rle_decode(encoded):
    decoded = []
    i = 0
    while i < len(encoded):
        count = int(encoded[i])
        char = encoded[i + 1]
        decoded.append(char * count)
        i += 2
    return ''.join(decoded)

if __name__ == '__main__':
    test_strings = [
        'AABCCCD',
        'AAAAAAAAAABBBCCCCD',
        'XXYYZZ',
        'ABC',
        'AAAAABBBBBBBBBBBBBBBBBBBBBBBBBB',
        ''
    ]
    for s in test_strings:
        encoded = rle_encode(s)
        decoded = rle_decode(encoded)
        print(f"Original: {repr(s)}")
        print(f"Encoded:  {repr(encoded)}")
        print(f"Decoded:  {repr(decoded)}")
        print(f"Fidelity: {s == decoded}")
        print()