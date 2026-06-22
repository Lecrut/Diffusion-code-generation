def rle_compress(text):
    if not text:
        return ""
    result = []
    count = 1
    length = len(text)
    for i in range(length):
        if i + 1 < length and text[i] == text[i + 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(text[i])
            count = 1
    return "".join(result)

def rle_decompress(compressed):
    result = []
    i = 0
    length = len(compressed)
    while i < length:
        count = 0
        while i < length and compressed[i].isdigit():
            count = count * 10 + int(compressed[i])
            i += 1
        if i < length:
            result.append(compressed[i] * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_text = "WWWWWWWWWWWWBWWWWWWWWWWWWWWBWWWBWWWWWWWWWWWWWWWW"
    compressed = rle_compress(sample_text)
    decompressed = rle_decompress(compressed)
    print(compressed)
    print(decompressed)