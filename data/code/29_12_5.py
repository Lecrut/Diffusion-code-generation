def encode_repeated_chars(s):
    if not s:
        return
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded = f"{count}{current_char}" if count > 1 else current_char
            yield encoded
            current_char = s[i]
            count = 1
    encoded = f"{count}{current_char}" if count > 1 else current_char
    yield encoded

if __name__ == '__main__':
    test_string = "aaabbbcccc"
    result = list(encode_repeated_chars(test_string))
    print(result)