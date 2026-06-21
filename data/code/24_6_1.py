def compress_rle(data: str) -> str:
    if not data:
        return ""
    compressed = []
    count = 1
    current_char = data[0]
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1
    compressed.append(f"{current_char}{count}")
    return "".join(compressed)

def decompress_rle(data: str) -> str:
    if not data:
        return ""
    decompressed = []
    i = 0
    while i < len(data):
        char = data[i]
        i += 1
        num_str = ""
        while i < len(data) and data[i].isdigit():
            num_str += data[i]
            i += 1
        if not num_str:
            num_str = "1"
        count = int(num_str)
        decompressed.append(char * count)
    return "".join(decompressed)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    compressed_result = compress_rle(sample_string)
    decompressed_result = decompress_rle(compressed_result)
    print(compressed_result)
    print(decompressed_result)