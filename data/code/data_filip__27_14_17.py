def rle_encode(s):
    if not s:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

def rle_decode(s):
    decoded = []
    i = 0
    while i < len(s):
        count = 0
        while i < len(s) and s[i].isdigit():
            count = count * 10 + int(s[i])
            i += 1
        if i < len(s):
            char = s[i]
            decoded.append(char * count)
            i += 1
    return "".join(decoded)

if __name__ == '__main__':
    sample_string = "AAABBBCCCCDDDDD"
    encoded = rle_encode(sample_string)
    decoded = rle_decode(encoded)
    print(encoded)
    print(decoded)