def compress_text(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            if count > 1:
                result.append(str(count))
            current_char = char
            count = 1
    result.append(current_char)
    if count > 1:
        result.append(str(count))
    return "".join(result)

if __name__ == '__main__':
    sample1 = "aabcccccaaa"
    sample2 = "abcdef"
    sample3 = ""
    sample4 = "a"
    print(compress_text(sample1))
    print(compress_text(sample2))
    print(compress_text(sample3))
    print(compress_text(sample4))