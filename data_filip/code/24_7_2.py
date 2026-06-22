def rle_compress(data):
    if not data:
        return ""
    compressed = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = data[i]
            count = 1
    compressed.append(f"{current_char}{count}")
    return "".join(compressed)

def rle_decompress(compressed):
    if not compressed:
        return ""
    decompressed = []
    i = 0
    while i < len(compressed):
        char = compressed[i]
        i += 1
        num_str = []
        while i < len(compressed) and compressed[i].isdigit():
            num_str.append(compressed[i])
            i += 1
        if not num_str:
            num_str.append("1")
        count = int("".join(num_str))
        decompressed.append(char * count)
    return "".join(decompressed)

if __name__ == "__main__":
    sample_input = "0011100"
    compressed_result = rle_compress(sample_input)
    decompressed_result = rle_decompress(compressed_result)
    print(compressed_result)
    print(decompressed_result)