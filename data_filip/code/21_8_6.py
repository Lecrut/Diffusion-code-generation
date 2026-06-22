def rle_encode(text: str) -> list:
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

if __name__ == '__main__':
    sample_text = "aaabbc"
    encoded_data = rle_encode(sample_text)
    print(encoded_data)