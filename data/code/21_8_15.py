def rle_encode(text: str) -> list[tuple[str, int]]:
    if not text:
        return []
    result = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

def rle_decode(encoded_data: list[tuple[str, int]]) -> str:
    if not encoded_data:
        return ""
    result = []
    for char, count in encoded_data:
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbc"
    encoded = rle_encode(sample_text)
    decoded = rle_decode(encoded)
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Match: {sample_text == decoded}")