def encode_repeated_chars(text):
    if not text:
        return
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            if count > 1:
                yield f"{current_char}{count}"
            else:
                yield current_char
            current_char = text[i]
            count = 1
    if count > 1:
        yield f"{current_char}{count}"
    else:
        yield current_char

if __name__ == '__main__':
    sample_text = "aaabbcdddeeffg"
    result = list(encode_repeated_chars(sample_text))
    print(result)