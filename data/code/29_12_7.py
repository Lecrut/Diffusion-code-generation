def encode_segments(s):
    if not s:
        return
    count = 0
    current_char = s[0]
    for char in s:
        if char == current_char:
            count += 1
        else:
            yield f"{count}{current_char}"
            current_char = char
            count = 1
    yield f"{count}{current_char}"

if __name__ == '__main__':
    test_string = "aaabbbcc"
    result = list(encode_segments(test_string))
    print(result)