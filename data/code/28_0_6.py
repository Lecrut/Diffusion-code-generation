def rle_encode(text):
    if not text:
        return []
    result = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_text = "aaabbbcccd"
    compressed = rle_encode(sample_text)
    print(compressed)