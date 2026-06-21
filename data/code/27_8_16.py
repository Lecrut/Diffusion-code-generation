def encode_rle(input_string):
    if not input_string:
        return []
    encoded = []
    count = 1
    length = len(input_string)
    for index in range(1, length):
        current_char = input_string[index]
        prev_char = input_string[index - 1]
        if current_char == prev_char:
            count += 1
        else:
            encoded.append((prev_char, count))
            count = 1
    encoded.append((input_string[-1], count))
    return encoded

if __name__ == '__main__':
    sample_data = 'WWWWWWWWWWWWWBWWWWWWWWWWWWWWWBWWWWWWWWWWWWWWCCCCCCCCCC'
    result = encode_rle(sample_data)
    print(result)