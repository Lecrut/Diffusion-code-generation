def rle_compress(text):
    if not text:
        return ""
    compressed = []
    count = 1
    current_char = text[0]
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            compressed.append(f"{count}{current_char}")
            current_char = text[i]
            count = 1
    compressed.append(f"{count}{current_char}")
    return "".join(compressed)

if __name__ == "__main__":
    sample_text = "aaabbcdddd"
    result = rle_compress(sample_text)
    print(result)