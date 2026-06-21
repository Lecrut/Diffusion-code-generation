def compress_rle(data):
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

def decompress_rle(data):
    if not data:
        return ""
    decompressed = []
    i = 0
    while i < len(data):
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        if not count_str:
            raise ValueError("Invalid RLE format: missing count")
        if i >= len(data):
            raise ValueError("Invalid RLE format: missing character")
        char = data[i]
        decompressed.append(char * int(count_str))
        i += 1
    return "".join(decompressed)

if __name__ == "__main__":
    sample_data = "0011100"
    compressed_result = compress_rle(sample_data)
    decompressed_result = decompress_rle(compressed_result)
    print(f"Original: {sample_data}")
    print(f"Compressed: {compressed_result}")
    print(f"Decompressed: {decompressed_result}")