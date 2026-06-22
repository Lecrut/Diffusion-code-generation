def rle_encode_case_insensitive(text):
    if not text:
        return ""
    normalized = text.lower()
    if not normalized:
        return ""
    result = []
    count = 1
    current_char = normalized[0]
    for i in range(1, len(normalized)):
        char = normalized[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_text = "AAbBBcccDDD"
    encoded = rle_encode_case_insensitive(sample_text)
    print(encoded)