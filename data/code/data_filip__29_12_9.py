def encode_repeated_chars(s):
    if not s:
        return
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            yield current_char if count == 1 else f"{current_char}{count}"
            current_char = char
            count = 1
    yield current_char if count == 1 else f"{current_char}{count}"

if __name__ == '__main__':
    test_string = "aaabbbcccaaaa"
    result = list(encode_repeated_chars(test_string))
    print(result)