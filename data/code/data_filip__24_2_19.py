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

if __name__ == "__main__":
    test_strings = ["AAABBBCCCC", "Wwwwww", "111222", ""]
    for original in test_strings:
        encoded = rle_encode(original)
        decoded = rle_decode(encoded)
        print(f"Original: {original}")
        print(f"Encoded: {encoded}")
        print(f"Decoded: {decoded}")
        print(f"Match: {original == decoded}")
        print("---")