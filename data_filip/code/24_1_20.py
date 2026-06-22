def decompress_rle(compressed):
    decompressed = []
    i = 0
    while i < len(compressed):
        if compressed[i].isdigit():
            count_str = ""
            while i < len(compressed) and compressed[i].isdigit():
                count_str += compressed[i]
                i += 1
            count = int(count_str)
            if i < len(compressed):
                char = compressed[i]
                decompressed.append(char * count)
                i += 1
        else:
            decompressed.append(compressed[i])
            i += 1
    return "".join(decompressed)

if __name__ == '__main__':
    sample_compressed = "3A2B5C"
    print(decompress_rle(sample_compressed))