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
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def rle_decode(encoded):
    if not encoded:
        return ""
    decoded = []
    i = 0
    while i < len(encoded):
        count = 0
        while i < len(encoded) and encoded[i].isdigit():
            count = count * 10 + int(encoded[i])
            i += 1
        char = encoded[i]
        decoded.append(char * count)
        i += 1
    return "".join(decoded)

if __name__ == '__main__':
    test_cases = [
        "AAAABBBCCDAA",
        "A",
        "ABC",
        "AAABBBCCC",
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
        "AABCCDEFFGGGHHHHIIIIJJJJJKKKKKKLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"
    ]
    for case in test_cases:
        encoded = rle_encode(case)
        decoded = rle_decode(encoded)
        print(f"Original: {case}")
        print(f"Encoded:  {encoded}")
        print(f"Decoded:  {decoded}")
        print(f"Match: {case == decoded}")
        print()