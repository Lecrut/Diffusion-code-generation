def bidirectional_rle(text):
    compressed = rle_compress(text)
    decompressed = rle_decompress(compressed)
    return compressed, decompressed

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
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1
    compressed.append(f"{current_char}{count}")
    return "".join(compressed)

def rle_decompress(compressed):
    decompressed = []
    i = 0
    while i < len(compressed):
        char = compressed[i]
        i += 1
        count_str = ""
        while i < len(compressed) and compressed[i].isdigit():
            count_str += compressed[i]
            i += 1
        count = int(count_str) if count_str else 1
        decompressed.append(char * count)
    return "".join(decompressed)

if __name__ == '__main__':
    sample_text = "AAABBBCCCCAAB"
    result = bidirectional_rle(sample_text)
    print(result)