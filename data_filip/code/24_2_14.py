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
            encoding.append(f"{count}{prev_char}")
            prev_char = char
            count = 1
    encoding.append(f"{count}{prev_char}")
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
            count = int(count_str)
            char = data[i]
            decoded.append(char * count)
            i += 1
    return "".join(decoded)

if __name__ == '__main__':
    test_cases = [
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
        "AABBBCCCC",
        "ABC",
        "AAAABBBCCDAA",
        ""
    ]
    for original in test_cases:
        encoded = rle_encode(original)
        decoded = rle_decode(encoded)
        print(f"Original: {original}")
        print(f"Encoded:  {encoded}")
        print(f"Decoded:  {decoded}")
        print(f"Match:    {original == decoded}")
        print("-" * 30)