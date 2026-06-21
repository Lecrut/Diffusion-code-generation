def rle_compress(data):
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

def rle_decompress(compressed_data):
    if not compressed_data:
        return ""
    result = []
    i = 0
    while i < len(compressed_data):
        num_str = ""
        while i < len(compressed_data) and compressed_data[i].isdigit():
            num_str += compressed_data[i]
            i += 1
        if i < len(compressed_data):
            char = compressed_data[i]
            count = int(num_str)
            result.append(char * count)
            i += 1
    return "".join(result)

def process_bidirectional_rle(data):
    compressed = rle_compress(data)
    decompressed = rle_decompress(compressed)
    return compressed, decompressed

if __name__ == '__main__':
    sample_string = "AAABBBCCCCDDDD"
    compressed_version, restored_version = process_bidirectional_rle(sample_string)
    print(f"Original: {sample_string}")
    print(f"Compressed: {compressed_version}")
    print(f"Restored: {restored_version}")
    print(f"Integrity Check: {sample_string == restored_version}")