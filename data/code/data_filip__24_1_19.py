def decompress_rle(compressed_data):
    if not compressed_data:
        return ""
    result = []
    i = 0
    while i < len(compressed_data):
        if not compressed_data[i].isdigit():
            return ""
        num_str = ""
        while i < len(compressed_data) and compressed_data[i].isdigit():
            num_str += compressed_data[i]
            i += 1
        if i >= len(compressed_data):
            return ""
        char = compressed_data[i]
        count = int(num_str)
        result.append(char * count)
        i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "12a5b3c"
    output = decompress_rle(sample_input)
    print(output)