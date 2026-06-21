def rle_compress(data: str) -> str:
    if not data:
        return ""
    result = []
    length = len(data)
    i = 0
    while i < length:
        current_char = data[i]
        count = 1
        while i + 1 < length and data[i + 1] == current_char:
            count += 1
            i += 1
        result.append(f"{count}{current_char}")
        i += 1
    return "".join(result)

def rle_decompress(compressed: str) -> str:
    if not compressed:
        return ""
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
    sample_text = "AAABBBBCCCCCDDDDDDDE"
    compressed = rle_compress(sample_text)
    decompressed = rle_decompress(compressed)
    print(f"Original: {sample_text}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Match: {sample_text == decompressed}")