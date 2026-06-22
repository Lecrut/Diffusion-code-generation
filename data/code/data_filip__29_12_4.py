def encode_segments(text):
    if not text:
        return
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                yield f"{count}{current_char}"
            else:
                yield current_char
            current_char = char
            count = 1
    if count > 1:
        yield f"{count}{current_char}"
    else:
        yield current_char

if __name__ == '__main__':
    result = list(encode_segments("AAABBBCCD"))
    print(result)