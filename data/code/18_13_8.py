def rle_encode(s):
    if not s:
        return []
    encoded = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            yield (count, current_char)
            current_char = char
            count = 1
    yield (count, current_char)

def rle_decode(encoded):
    decoded = []
    for count, char in encoded:
        yield from (char for _ in range(count))

def encode_string(s):
    return list(rle_encode(s))

def decode_string(encoded):
    return ''.join(rle_decode(encoded))

if __name__ == '__main__':
    sample_strings = [
        "AAABBBCCD",
        "ABC",
        "AAAAAAAA",
        "",
        "A"
    ]
    for s in sample_strings:
        encoded = encode_string(s)
        decoded = decode_string(encoded)
        print(f"Original: {s!r} -> Encoded: {encoded} -> Decoded: {decoded!r}")