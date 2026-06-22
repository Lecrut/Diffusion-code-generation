def rle_decompress(compressed_string):
    decompressed = []
    i = 0
    while i < len(compressed_string):
        count_str = ""
        while i < len(compressed_string) and compressed_string[i].isdigit():
            count_str += compressed_string[i]
            i += 1
        if count_str:
            count = int(count_str)
        else:
            count = 1
        if i < len(compressed_string):
            char = compressed_string[i]
            decompressed.append(char * count)
            i += 1
    return "".join(decompressed)

if __name__ == '__main__':
    sample_compressed = "3a4b2c1d5e"
    result = rle_decompress(sample_compressed)
    print(result)