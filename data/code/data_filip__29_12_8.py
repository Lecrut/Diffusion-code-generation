def encode_repeated_chars(text):
    if not text:
        return
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            yield (current_char, count)
            current_char = char
            count = 1
    yield (current_char, count)

if __name__ == '__main__':
    sample_text = 'aaabbbcc'
    result = list(encode_repeated_chars(sample_text))
    print(result)