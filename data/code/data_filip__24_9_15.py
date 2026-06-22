def run_length_encode(text):
    if not text:
        return ""

    compressed_parts = []
    current_char = text[0]
    count = 1

    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            compressed_parts.append(f"{count}{current_char}")
            current_char = char
            count = 1

    compressed_parts.append(f"{count}{current_char}")
    return "".join(compressed_parts)

if __name__ == "__main__":
    text = "AAABBBCCCD"
    result = run_length_encode(text)
    print(result)