import sys

def compress_rle(data):
    if not data:
        return ""
    compressed = []
    count = 1
    prev = data[0]
    for char in data[1:]:
        if char == prev:
            count += 1
        else:
            compressed.append(f"{count}{prev}")
            count = 1
            prev = char
    compressed.append(f"{count}{prev}")
    return "".join(compressed)

def decompress_rle(data):
    if not data:
        return ""
    decompressed = []
    i = 0
    n = len(data)
    while i < n:
        num_str = ""
        while i < n and data[i].isdigit():
            num_str += data[i]
            i += 1
        if i < n:
            char = data[i]
            count = int(num_str)
            decompressed.append(char * count)
            i += 1
    return "".join(decompressed)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAABBB"
    compressed_version = compress_rle(sample_string)
    decompressed_version = decompress_rle(compressed_version)
    print(f"Original: {sample_string}")
    print(f"Compressed: {compressed_version}")
    print(f"Decompressed: {decompressed_version}")
    print(f"Match: {sample_string == decompressed_version}")