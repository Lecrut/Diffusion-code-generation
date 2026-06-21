def compress_rle(data):
    if not data:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed.append(f"{data[i - 1]}{count}")
            count = 1
    compressed.append(f"{data[-1]}{count}")
    return "".join(compressed)

def decompress_rle(data):
    if not data:
        return ""
    decompressed = []
    i = 0
    while i < len(data):
        char = data[i]
        i += 1
        num_str = []
        while i < len(data) and data[i].isdigit():
            num_str.append(data[i])
            i += 1
        if not num_str:
            num_str.append("1")
        count = int("".join(num_str))
        decompressed.append(char * count)
    return "".join(decompressed)

def process_and_verify(data):
    compressed = compress_rle(data)
    decompressed = decompress_rle(compressed)
    is_valid = data == decompressed
    return compressed, decompressed, is_valid

if __name__ == "__main__":
    sample_input = "AAABBBCCCA"
    compressed_str, decompressed_str, valid = process_and_verify(sample_input)
    print(compressed_str)
    print(decompressed_str)
    print(valid)