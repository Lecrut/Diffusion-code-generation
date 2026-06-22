def rle_compress(text):
    if not text:
        return ""
    compressed = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{count}{current_char}")
            current_char = char
            count = 1
    compressed.append(f"{count}{current_char}")
    return "".join(compressed)

if __name__ == '__main__':
    sample_text = "AAABBBCCD"
    result = rle_compress(sample_text)
    print(result)