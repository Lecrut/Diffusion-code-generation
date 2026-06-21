def encode_rle(data):
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    result.append(str(count))
    result.append(current_char)
    return "".join(result)

def decode_rle(data):
    if not data:
        return ""
    result = []
    num_str = []
    for char in data:
        if char.isdigit():
            num_str.append(char)
        else:
            count = int("".join(num_str))
            result.append(char * count)
            num_str = []
    return "".join(result)

if __name__ == '__main__':
    encoded = encode_rle("aabcccccaaa")
    print(encoded)
    decoded = decode_rle("2a1b5c3a")
    print(decoded)