def rle_compress(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def rle_decompress(text):
    if not text:
        return ""
    result = []
    i = 0
    length = len(text)
    while i < length:
        j = i
        while j < length and text[j].isdigit():
            j += 1
        if j == length:
            break
        count = int(text[i:j])
        char = text[j]
        result.append(char * count)
        i = j + 1
    return "".join(result)

if __name__ == '__main__':
    sample_text = "WWWWWWWWWWWWBWWWWWWWWWWWWWWBWWW"
    compressed = rle_compress(sample_text)
    decompressed = rle_decompress(compressed)
    print(f"Original: {sample_text}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")