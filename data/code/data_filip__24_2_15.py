def rle_encode(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char and count < 255:
            count += 1
        else:
            encoded.append((count, current_char))
            current_char = char
            count = 1
    encoded.append((count, current_char))
    return ''.join(f"{count}{char}" for count, char in encoded)

def rle_decode(encoded):
    if not encoded:
        return ""
    decoded = []
    i = 0
    while i < len(encoded):
        count = ""
        while i < len(encoded) and encoded[i].isdigit():
            count += encoded[i]
            i += 1
        if count:
            count = int(count)
        else:
            count = 1
        if i < len(encoded):
            char = encoded[i]
            i += 1
            decoded.append(char * count)
        else:
            break
    return ''.join(decoded)

if __name__ == '__main__':
    test_cases = [
        "AABCCDDD",
        "AAAAABBBCCCCCC",
        "XYZ",
        "AAAAAAAAAAAAAAAAAAAAAAAAAA",
        "",
        "A",
        "AABBCCDDEE",
        "112233"
    ]
    for test in test_cases:
        encoded = rle_encode(test)
        decoded = rle_decode(encoded)
        print(f"Original: {repr(test)}")
        print(f"Encoded: {repr(encoded)}")
        print(f"Decoded: {repr(decoded)}")
        print(f"Fidelity: {test == decoded}")
        print()