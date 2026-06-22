def encode_repeated_chars(s):
    if not s:
        return
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            yield (current_char, count)
            current_char = char
            count = 1
    yield (current_char, count)

if __name__ == '__main__':
    sample_string = "aaabbcddde"
    encoded_segments = list(encode_repeated_chars(sample_string))
    print(encoded_segments)