def rle_encode(text):
    if not text:
        return ""
    encoded = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
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
    length = len(encoded)
    while i < length:
        num_str = []
        while i < length and encoded[i].isdigit():
            num_str.append(encoded[i])
            i += 1
        if i < length:
            char = encoded[i]
            i += 1
            count = int("".join(num_str)) if num_str else 1
            decoded.append(char * count)
    return "".join(decoded)

if __name__ == '__main__':
    original = "aabcccccaaa"
    encoded = rle_encode(original)
    decoded = rle_decode(encoded)
    print(original == decoded)