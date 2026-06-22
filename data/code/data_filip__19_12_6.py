import itertools

def rle_compress(text):
    if not text:
        return ""
    compressed = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                compressed.append(str(count))
            compressed.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        compressed.append(str(count))
    compressed.append(current_char)
    return "".join(compressed)

def rle_decompress(compressed):
    if not compressed:
        return ""
    decompressed = []
    i = 0
    while i < len(compressed):
        count_str = []
        while i < len(compressed) and compressed[i].isdigit():
            count_str.append(compressed[i])
            i += 1
        count = int("".join(count_str)) if count_str else 1
        if i < len(compressed):
            char = compressed[i]
            decompressed.append(char * count)
            i += 1
    return "".join(decompressed)

if __name__ == '__main__':
    sample_text = "AAABBBCCDAAEEEEE"
    compressed = rle_compress(sample_text)
    decompressed = rle_decompress(compressed)
    print(compressed)
    print(decompressed)