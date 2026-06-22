def rle_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    current_char = s[0]
    length = len(s)
    for i in range(1, length):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{current_char}")
            else:
                result.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        result.append(f"{count}{current_char}")
    else:
        result.append(current_char)
    return "".join(result)

def rle_decode(s):
    if not s:
        return ""
    result = []
    i = 0
    length = len(s)
    while i < length:
        char = s[i]
        if char.isdigit():
            num_str = ""
            while i < length and s[i].isdigit():
                num_str += s[i]
                i += 1
            multiplier = int(num_str)
            char = s[i]
            i += 1
            result.append(char * multiplier)
        else:
            result.append(char)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    original = "AAABBBCCCDAA"
    encoded = rle_encode(original)
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded)