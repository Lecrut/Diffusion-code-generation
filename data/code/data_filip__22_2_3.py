def decompress_rle(encoded_string):
    if not encoded_string:
        return ""
    result = []
    i = 0
    n = len(encoded_string)
    while i < n:
        num_start = i
        while i < n and encoded_string[i].isdigit():
            i += 1
        if i == num_start:
            result.append(encoded_string[i])
            i += 1
        else:
            count = int(encoded_string[num_start:i])
            result.append(encoded_string[i] * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "4a3b2c1d"
    print(decompress_rle(sample_input))