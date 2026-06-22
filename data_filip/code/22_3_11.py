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
    decoded = []
    i = 0
    while i < len(data):
        if not data[i].isdigit():
            decoded.append(data[i])
            i += 1
        else:
            count = ""
            while i < len(data) and data[i].isdigit():
                count += data[i]
                i += 1
            if i < len(data):
                char = data[i]
                decoded.append(char * int(count))
                i += 1
    return "".join(decoded)

if __name__ == '__main__':
    sample = "AAABBBCCD"
    encoded = rle_encode(sample)
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded)