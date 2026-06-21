def encode_rle(s):
    if not s:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def decode_rle(encoded):
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
            if i < len(encoded):
                decoded.append(encoded[i] * count)
                i += 1
    return "".join(decoded)

if __name__ == "__main__":
    sample = "AAABBBCCD"
    encoded = encode_rle(sample)
    decoded = decode_rle(encoded)
    print(encoded)
    print(decoded)