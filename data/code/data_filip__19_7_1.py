def bidirectional_rle_process(input_string):
    def compress_rle(s):
        if not s:
            return ""
        compressed = []
        current_char = s[0]
        count = 1
        for char in s[1:]:
            if char == current_char:
                count += 1
            else:
                compressed.append((current_char, count))
                current_char = char
                count = 1
        compressed.append((current_char, count))
        return compressed

    def decompress_rle(compressed_data):
        decompressed = []
        for char, count in compressed_data:
            decompressed.append(char * count)
        return "".join(decompressed)

    compressed = compress_rle(input_string)
    decompressed = decompress_rle(compressed)
    return compressed, decompressed

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    result = bidirectional_rle_process(sample_string)
    print(result)