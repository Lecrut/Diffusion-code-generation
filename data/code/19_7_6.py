def run_bidirectional_rle(input_string):
    compressed = compress_rle(input_string)
    decompressed = decompress_rle(compressed)
    return {
        "original": input_string,
        "compressed": compressed,
        "decompressed": decompressed,
        "integrity": input_string == decompressed
    }

def compress_rle(s):
    if not s:
        return []
    result = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = s[i]
            count = 1
    result.append((current_char, count))
    return result

def decompress_rle(rle_data):
    result = []
    for char, count in rle_data:
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaaabbbcccd"
    result = run_bidirectional_rle(sample_string)
    print(result)