def rle_encode(text):
    if not text:
        return ""
    result = []
    count = 1
    current_char = text[0]
    length = len(text)
    for i in range(1, length):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
                result.append(current_char)
            else:
                result.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        result.append(str(count))
        result.append(current_char)
    else:
        result.append(current_char)
    return "".join(result)

def rle_decode(text):
    if not text:
        return ""
    result = []
    length = len(text)
    i = 0
    while i < length:
        char = text[i]
        if char.isdigit():
            count = 0
            while i < length and text[i].isdigit():
                count = count * 10 + int(text[i])
                i += 1
            result.append(char * count)
        else:
            result.append(char)
        i += 1
    return "".join(result)

if __name__ == '__main__':
    sample = "aaabbc"
    encoded = rle_encode(sample)
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded)