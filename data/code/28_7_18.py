def rle_generator(data):
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
    sample_string = "AAABBBCCCCDDEEE"
    encoded_list = list(rle_generator(sample_string))
    print(encoded_list)