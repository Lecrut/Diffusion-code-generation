def compress_rle(data: str) -> str:
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def decompress_rle(data: str) -> str:
    if not data:
        return ""
    result = []
    count_str = []
    for char in data:
        if char.isdigit():
            count_str.append(char)
        else:
            count = int("".join(count_str))
            result.append(char * count)
            count_str = []
    return "".join(result)

def run_compression_demo():
    original = "AAABBBCCDAA"
    compressed = compress_rle(original)
    decompressed = decompress_rle(compressed)
    return {"original": original, "compressed": compressed, "decompressed": decompressed, "match": original == decompressed}

if __name__ == '__main__':
    print(run_compression_demo())