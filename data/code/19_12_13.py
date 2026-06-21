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
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    return "".join(result)

def rle_decompress(compressed):
    if not compressed:
        return ""
    result = []
    i = 0
    while i < len(compressed):
        if compressed[i].isdigit():
            num_str = ""
            while i < len(compressed) and compressed[i].isdigit():
                num_str += compressed[i]
                i += 1
            count = int(num_str)
            if i < len(compressed):
                result.append(compressed[i] * count)
                i += 1
        else:
            result.append(compressed[i])
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_text = "AAABBBCCCD"
    compressed = rle_compress(sample_text)
    decompressed = rle_decompress(compressed)
    print(compressed)
    print(decompressed)