import re
from typing import List, Tuple

def rle_encode(text: str) -> List[Tuple[str, int]]:
    if not text:
        return []

    encoded = []
    current_char = text[0]
    count = 1

    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1

    encoded.append((current_char, count))
    return encoded

def rle_decode(encoded_data: List[Tuple[str, int]]) -> str:
    decoded_parts = []

    for char, count in encoded_data:
        decoded_parts.append(char * count)

    return "".join(decoded_parts)

def rle_compress(text: str) -> str:
    encoded = rle_encode(text)
    compressed_parts = []

    for char, count in encoded:
        if count > 1:
            compressed_parts.append(f"{count}{char}")
        else:
            compressed_parts.append(char)

    return "".join(compressed_parts)

def rle_expand(compressed: str) -> str:
    if not compressed:
        return ""

    pattern = re.compile(r"(\d+)?([A-Za-z0-9])")
    matches = pattern.findall(compressed)
    decoded_parts = []

    for count_str, char in matches:
        count = int(count_str) if count_str else 1
        decoded_parts.append(char * count)

    return "".join(decoded_parts)

def rle_compress_string(text: str) -> str:
    encoded = rle_encode(text)
    result_parts = []

    for char, count in encoded:
        if count == 1:
            result_parts.append(char)
        else:
            result_parts.append(f"{count}{char}")

    return "".join(result_parts)

def rle_expand_string(compressed: str) -> str:
    if not compressed:
        return ""

    result = []
    current_num = []

    for char in compressed:
        if char.isdigit():
            current_num.append(char)
        else:
            count = int("".join(current_num)) if current_num else 1
            result.append(char * count)
            current_num = []

    return "".join(result)

if __name__ == '__main__':
    sample_text = "aabcccccaaa"
    encoded_result = rle_encode(sample_text)
    decoded_result = rle_decode(encoded_result)
    compressed_result = rle_compress(sample_text)
    expanded_result = rle_expand(compressed_result)

    print(encoded_result)
    print(decoded_result)
    print(compressed_result)
    print(expanded_result)