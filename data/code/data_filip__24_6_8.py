import re

def compress_rle(text: str) -> str:
    if not text:
        return ""
    result = []
    count = 1
    current_char = text[0]
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def decompress_rle(rle_string: str) -> str:
    if not rle_string:
        return ""
    result = []
    for count_str, char in re.findall(r"(\d+)(\D)", rle_string):
        result.append(char * int(count_str))
    return "".join(result)

if __name__ == '__main__':
    original = "AAABBBCCCDAA"
    compressed = compress_rle(original)
    decompressed = decompress_rle(compressed)
    print(decompressed)