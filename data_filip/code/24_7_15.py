def compress_rle(data: str) -> str:
    if not data:
        return ""
    compressed = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{count}{current_char}")
            current_char = char
            count = 1
    compressed.append(f"{count}{current_char}")
    return "".join(compressed)

def decompress_rle(data: str) -> str:
    if not data:
        return ""
    decompressed = []
    i = 0
    while i < len(data):
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        if i >= len(data):
            break
        char = data[i]
        count = int(count_str)
        decompressed.append(char * count)
        i += 1
    return "".join(decompressed)

if __name__ == '__main__':
    sample_input = "0011100"
    compressed_result = compress_rle(sample_input)
    decompressed_result = decompress_rle(compressed_result)
    print(f"Original: {sample_input}")
    print(f"Compressed: {compressed_result}")
    print(f"Decompressed: {decompressed_result}")