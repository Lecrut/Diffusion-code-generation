def decompress_rle(encoded_string):
    if not encoded_string:
        return []
    result = []
    i = 0
    length = len(encoded_string)
    while i < length:
        digit_start = i
        while i < length and encoded_string[i].isdigit():
            i += 1
        count = int(encoded_string[digit_start:i])
        char = encoded_string[i]
        i += 1
        result.extend([char] * count)
    return result

if __name__ == '__main__':
    sample_input = "4a2b3c1d"
    output = decompress_rle(sample_input)
    print(output)