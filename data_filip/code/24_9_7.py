def compress_rle(text):
    if not text:
        return ""

    compressed = []
    current_char = text[0]
    count = 1
    length = len(text)
    i = 1

    while i < length:
        char = text[i]
        if char == current_char:
            count += 1
        else:
            compressed.append(str(count) + current_char)
            current_char = char
            count = 1
        i += 1

    compressed.append(str(count) + current_char)
    return "".join(compressed)

if __name__ == "__main__":
    sample_text = "AAAAABBBCCDAA"
    result = compress_rle(sample_text)
    print(result)