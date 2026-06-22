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
    while i < len(data):
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        if count_str:
            count = int(count_str)
        else:
            count = 1
        if i < len(data):
            char = data[i]
            result.append(char * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    original_string = "AAABBBCCDAA"
    compressed = rle_compress(original_string)
    decompressed = rle_decompress(compressed)
    print(decompressed)