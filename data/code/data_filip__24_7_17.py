def compress_rle(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def decompress_rle(s):
    if not s:
        return ""
    result = []
    i = 0
    n = len(s)
    while i < n:
        num_str = []
        while i < n and s[i].isdigit():
            num_str.append(s[i])
            i += 1
        count = int("".join(num_str))
        char = s[i]
        i += 1
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    original = "0011100"
    compressed = compress_rle(original)
    decompressed = decompress_rle(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    empty = ""
    print(f"Empty Compressed: {compress_rle(empty)}")
    single = "1"
    print(f"Single Compressed: {compress_rle(single)}")
    print(f"Single Decompressed: {decompress_rle(compress_rle(single))}")