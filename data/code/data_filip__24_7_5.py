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
            result.append(f"{current_char}{count}")
            current_char = data[i]
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

def decompress_rle(data: str) -> str:
    if not data:
        return ""
    result = []
    i = 0
    while i < len(data):
        if i + 1 >= len(data):
            raise ValueError("Invalid RLE format: missing count")
        char = data[i]
        count_str = data[i + 1]
        if not count_str.isdigit():
            raise ValueError(f"Invalid RLE format: expected digit after character, got '{count_str}'")
        count = int(count_str)
        result.append(char * count)
        i += 2
    return "".join(result)

if __name__ == "__main__":
    sample_input = "0011100"
    compressed = compress_rle(sample_input)
    decompressed = decompress_rle(compressed)
    print(compressed)
    print(decompressed)