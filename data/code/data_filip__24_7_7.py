def compress_rle(data: str) -> str:
    if not data:
        return ""
    result = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def decompress_rle(data: str) -> str:
    if not data:
        return ""
    result = []
    i = 0
    while i < len(data):
        if not data[i].isdigit():
            return ""
        j = i
        while j < len(data) and data[j].isdigit():
            j += 1
        count = int(data[i:j])
        if j >= len(data):
            return ""
        char = data[j]
        result.append(char * count)
        i = j + 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "0011100"
    compressed = compress_rle(sample_input)
    decompressed = decompress_rle(compressed)
    print(compressed)
    print(decompressed)