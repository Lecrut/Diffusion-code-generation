def compress_rle(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 3:
                result.append(f"{count}{current_char}")
            else:
                result.append(f"{current_char}" * count)
            current_char = char
            count = 1
    if count > 3:
        result.append(f"{count}{current_char}")
    else:
        result.append(f"{current_char}" * count)
    return "".join(result)

def decompress_rle(compressed):
    if not compressed:
        return ""
    result = []
    i = 0
    n = len(compressed)
    while i < n:
        if compressed[i].isdigit():
            count_start = i
            while i < n and compressed[i].isdigit():
                i += 1
            count = int(compressed[count_start:i])
            char = compressed[i]
            result.append(char * count)
            i += 1
        else:
            result.append(compressed[i])
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_text = "AAABBBCCCDDEEEEEEFFFF"
    compressed = compress_rle(sample_text)
    print(f"Compressed: {compressed}")
    decompressed = decompress_rle(compressed)
    print(f"Decompressed: {decompressed}")
    print(f"Match: {sample_text == decompressed}")