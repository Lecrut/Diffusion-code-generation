def rle_compress(data):
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def rle_decompress(data):
    if not data:
        return ""
    result = []
    i = 0
    length = len(data)
    while i < length:
        count_str = ""
        while i < length and data[i].isdigit():
            count_str += data[i]
            i += 1
        if i >= length:
            break
        char = data[i]
        i += 1
        count = int(count_str) if count_str else 1
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    original = "0011100"
    compressed = rle_compress(original)
    decompressed = rle_decompress(compressed)
    print(decompressed)