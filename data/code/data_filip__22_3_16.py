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

def decode_rle(s):
    if not s:
        return ""
    decoded = []
    i = 0
    while i < len(s):
        count_str = ""
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        if count_str:
            count = int(count_str)
        else:
            count = 1
        if i < len(s):
            char = s[i]
            decoded.append(char * count)
            i += 1
        else:
            break
    return "".join(decoded)

if __name__ == '__main__':
    sample = "AAABBBCCD"
    encoded = encode_rle(sample)
    decoded = decode_rle(encoded)
    print(encoded)
    print(decoded)