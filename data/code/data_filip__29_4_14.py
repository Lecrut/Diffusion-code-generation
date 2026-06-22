def compress_text(text):
    if not text:
        return ''
    parts = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            if count > 1:
                parts.append(str(count))
            parts.append(current_char)
            current_char = text[i]
            count = 1
    if count > 1:
        parts.append(str(count))
    parts.append(current_char)
    return ''.join(parts)

if __name__ == '__main__':
    sample_text = "aaabbbcccdddddeeee"
    compressed = compress_text(sample_text)
    print(compressed)
    sample_text2 = "abcdef"
    compressed2 = compress_text(sample_text2)
    print(compressed2)
    sample_text3 = "aabbc"
    compressed3 = compress_text(sample_text3)
    print(compressed3)