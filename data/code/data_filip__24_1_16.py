def decompress_rle(compressed_string):
    if not compressed_string:
        return ""
    result = []
    i = 0
    while i < len(compressed_string):
        if not compressed_string[i].isdigit():
            return ""
        num_start = i
        while i < len(compressed_string) and compressed_string[i].isdigit():
            i += 1
        count = int(compressed_string[num_start:i])
        if i >= len(compressed_string):
            return ""
        char = compressed_string[i]
        i += 1
        if count < 0:
            return ""
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "4A3B2C1D"
    decompressed_output = decompress_rle(sample_input)
    print(decompressed_output)