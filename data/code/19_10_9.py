def compress_rle(input_string):
    if not input_string:
        return ""
    compressed = []
    current_char = input_string[0]
    count = 1
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(str(count) + current_char)
            current_char = char
            count = 1
    compressed.append(str(count) + current_char)
    return ''.join(compressed)

def decompress_rle(compressed_string):
    if not compressed_string:
        return ""
    decompressed = []
    count = ""
    for char in compressed_string:
        if char.isdigit():
            count += char
        else:
            if count:
                decompressed.append(char * int(count))
                count = ""
            else:
                decompressed.append(char)
    return ''.join(decompressed)

if __name__ == '__main__':
    sample_string = "AAABBBCCD"
    compressed = compress_rle(sample_string)
    print(compressed)
    decompressed = decompress_rle(compressed)
    print(decompressed)