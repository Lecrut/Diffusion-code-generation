def rle_encode(data: str) -> str:
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    return "".join(result)

def rle_decode(encoded: str) -> str:
    if not encoded:
        return ""
    result = []
    i = 0
    n = len(encoded)
    while i < n:
        count_str = []
        while i < n and encoded[i].isdigit():
            count_str.append(encoded[i])
            i += 1
        count = int("".join(count_str)) if count_str else 1
        if i < n:
            char = encoded[i]
            result.append(char * count)
            i += 1
        else:
            break
    return "".join(result)

if __name__ == '__main__':
    sample_data = "AAABBBCCCCD"
    encoded = rle_encode(sample_data)
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded)
    sample_data2 = "AABBBCCCC"
    encoded2 = rle_encode(sample_data2)
    print(encoded2)
    decoded2 = rle_decode(encoded2)
    print(decoded2)