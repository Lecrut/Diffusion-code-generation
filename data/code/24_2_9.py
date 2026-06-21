def rle_encode(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

def rle_decode(encoded):
    decoded = []
    i = 0
    while i < len(encoded):
        count = 0
        while i < len(encoded) and encoded[i].isdigit():
            count = count * 10 + int(encoded[i])
            i += 1
        if i < len(encoded):
            char = encoded[i]
            decoded.append(char * count)
            i += 1
    return "".join(decoded)

if __name__ == "__main__":
    test_cases = [
        "aaabbcddd",
        "abcdef",
        "aaaaa",
        "ababab",
        "hello world",
        "AABBCCDD",
        "",
        "single",
        "123123",
        "zzzzyyyyxxxx"
    ]
    for test in test_cases:
        encoded = rle_encode(test)
        decoded = rle_decode(encoded)
        print(test, "->", encoded, "->", decoded, "|", "Pass" if test == decoded else "Fail")