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

def rle_decode(data):
    decoded = []
    count = 0
    for char in data:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            decoded.append(char * count)
            count = 0
    return "".join(decoded)

if __name__ == '__main__':
    test_strings = [
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
        "AAABBCDD",
        "Z",
        "",
        "A123B"
    ]
    
    for original in test_strings:
        encoded = rle_encode(original)
        decoded = rle_decode(encoded)
        print(f"Original: {original}")
        print(f"Encoded: {encoded}")
        print(f"Decoded: {decoded}")
        print(f"Round-trip successful: {original == decoded}")
        print("-" * 40)