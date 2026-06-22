def rle_compress(data):
    if not data:
        return ""
    compressed = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = char
            count = 1
    compressed.append((current_char, count))
    return compressed

def rle_decompress(compressed):
    decompressed = []
    for char, count in compressed:
        decompressed.append(char * count)
    return "".join(decompressed)

def bidirectional_rle_test(input_string):
    compressed = rle_compress(input_string)
    decompressed = rle_decompress(compressed)
    return {
        "original": input_string,
        "compressed": compressed,
        "decompressed": decompressed,
        "integrity_verified": input_string == decompressed
    }

if __name__ == "__main__":
    sample_strings = [
        "aaaabbbccdaa",
        "hello world",
        "aabbccddeeff",
        "xyzyzyz",
        "",
        "a",
        "aaaaaaaaaa"
    ]
    results = []
    for s in sample_strings:
        result = bidirectional_rle_test(s)
        results.append(result)
    print(results)