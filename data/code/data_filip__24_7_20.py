def compress_rle(data):
    if not data:
        return ""
    compressed = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            compressed.append(f"{count}{current_char}")
            current_char = data[i]
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
        if i < len(data):
            char = data[i]
            count = int(count_str)
            decompressed.append(char * count)
        i += 1
    return "".join(decompressed)

if __name__ == '__main__':
    sample_input = '0011100'
    compressed_result = compress_rle(sample_input)
    decompressed_result = decompress_rle(compressed_result)
    print(compressed_result)
    print(decompressed_result)
    empty_test = compress_rle("")
    print(empty_test)
    single_test = compress_rle("5")
    print(single_test)
    decompress_single = decompress_rle("15")
    print(decompress_single)