def rle_compress(text):
    if not text:
        return ""
    result = []
    count = 1
    current_char = text[0]
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = text[i]
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

def rle_decompress(compressed_text):
    if not compressed_text:
        return ""
    result = []
    i = 0
    while i < len(compressed_text):
        char = compressed_text[i]
        i += 1
        count_str = []
        while i < len(compressed_text) and compressed_text[i].isdigit():
            count_str.append(compressed_text[i])
            i += 1
        if count_str:
            count = int("".join(count_str))
        else:
            count = 1
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_text = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    compressed = rle_compress(sample_text)
    decompressed = rle_decompress(compressed)
    print(compressed)
    print(decompressed)