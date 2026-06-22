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
    while i < len(encoded):
        count_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        if i < len(encoded):
            char = encoded[i]
            i += 1
            decoded.append(char * int(count_str))
    return "".join(decoded)

if __name__ == '__main__':
    sample = "aaabbcddd"
    encoded = rle_encode(sample)
    decoded = rle_decode(encoded)
    print(encoded)
    print(decoded)