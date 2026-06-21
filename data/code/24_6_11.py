import re

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

def decompress_rle(encoded: str) -> str:
    if not encoded:
        return ""
    parts = re.findall(r'(\d+)(\D)', encoded)
    return "".join(count * char for count, char in parts)

if __name__ == '__main__':
    original = "aaabbbcccd"
    compressed = compress_rle(original)
    decompressed = decompress_rle(compressed)
    print(compressed)
    print(decompressed)