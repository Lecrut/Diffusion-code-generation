def run_length_encode(text: str) -> list[tuple[str, int]]:
    if not text:
        return []

    encoded: list[tuple[str, int]] = []
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

if __name__ == '__main__':
    sample_text = "aabcccccaaa"
    result = run_length_encode(sample_text)
    print(result)