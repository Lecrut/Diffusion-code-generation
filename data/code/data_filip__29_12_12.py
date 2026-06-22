def encode_segments(s):
    if not s:
        return
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            yield f"{current_char}{count}"
            current_char = s[i]
            count = 1
    yield f"{current_char}{count}"

if __name__ == '__main__':
    test_string = "aaabbbcccaaa"
    result = list(encode_segments(test_string))
    print(result)