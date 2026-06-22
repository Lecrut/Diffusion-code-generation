def rle_encode(data):
    if not data:
        return ""
    encoding = []
    prev_char = data[0]
    count = 1
    for char in data[1:]:
        if char == prev_char:
            count += 1
        else:
            encoding.append(str(count) + prev_char)
            prev_char = char
            count = 1
    encoding.append(str(count) + prev_char)
    return "".join(encoding)

def rle_decode(data):
    if not data:
        return ""
    decoded = []
    i = 0
    while i < len(data):
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        if i < len(data):
            char = data[i]
            count = int(count_str)
            decoded.append(char * count)
            i += 1
    return "".join(decoded)

if __name__ == '__main__':
    test_cases = [
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
        "AABBBCCCC",
        "XYZ",
        "AAABBC",
        ""
    ]
    for test in test_cases:
        encoded = rle_encode(test)
        decoded = rle_decode(encoded)
        print(f"Original: {test}")
        print(f"Encoded:  {encoded}")
        print(f"Decoded:  {decoded}")
        print(f"Match: {test == decoded}")
        print("-" * 40)