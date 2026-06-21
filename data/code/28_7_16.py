def rle_encode(data):
    if not data:
        return
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            yield count, current_char
            current_char = char
            count = 1
    yield count, current_char

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    encoded_list = list(rle_encode(sample_string))
    print(encoded_list)
    sample_empty = ""
    encoded_empty = list(rle_encode(sample_empty))
    print(encoded_empty)