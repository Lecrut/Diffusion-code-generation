def rle_encode_lazy(s):
    if not s:
        return
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char and count < 255:
            count += 1
        else:
            yield (current_char, count)
            current_char = char
            count = 1
    yield (current_char, count)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    encoded_chunks = rle_encode_lazy(sample_string)
    result = list(encoded_chunks)
    print(result)