def encode_repeated_chars(s):
    if not s:
        return
    current = s[0]
    count = 1
    for char in s[1:]:
        if char == current:
            count += 1
        else:
            yield (current, count)
            current = char
            count = 1
    yield (current, count)

if __name__ == '__main__':
    test_string = "aaabbcddaabb"
    result = list(encode_repeated_chars(test_string))
    print(result)