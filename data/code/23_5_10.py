def compress_string(text):
    if text is None:
        raise TypeError("Input must be a string")
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if len(text) == 0:
        return ""
    compressed = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{count}{current_char}")
            current_char = char
            count = 1
    compressed.append(f"{count}{current_char}")
    return "".join(compressed)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    result = compress_string(sample_input)
    print(result)