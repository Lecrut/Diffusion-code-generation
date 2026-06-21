def rle_compress(data):
    if not data:
        return ""
    result = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def rle_decompress(data):
    if not data:
        return ""
    result = []
    i = 0
    while i < len(data):
        num_start = i
        while i < len(data) and data[i].isdigit():
            i += 1
        if num_start == i:
            break
        count = int(data[num_start:i])
        if i < len(data):
            char = data[i]
            result.append(char * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_text = "AAABBBCCCAAAABBBBBCCDDDD"
    compressed = rle_compress(sample_text)
    decompressed = rle_decompress(compressed)
    print(f"Original: {sample_text}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Integrity Check: {sample_text == decompressed}")