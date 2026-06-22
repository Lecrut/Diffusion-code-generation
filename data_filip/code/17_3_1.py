def rle_encode(text: str) -> str:
    if not text:
        return ""
    result = []
    count = 1
    current_char = text[0]
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbbccddeeff"
    encoded = rle_encode(sample_string)
    print(encoded)