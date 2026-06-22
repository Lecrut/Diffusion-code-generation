def compress_rle(text):
    if not text:
        return ""

    compressed = []
    current_char = text[0]
    count = 1

    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            compressed.append(str(count) + current_char)
            current_char = text[i]
            count = 1

    compressed.append(str(count) + current_char)
    return "".join(compressed)

if __name__ == '__main__':
    sample_text = "AAABBBCCCD"
    result = compress_rle(sample_text)
    print(result)