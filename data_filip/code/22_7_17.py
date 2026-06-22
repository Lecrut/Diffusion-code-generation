def decode_rle(compressed):
    if not compressed:
        return ""
    result = []
    i = 0
    n = len(compressed)
    while i < n:
        count = 0
        while i < n and compressed[i].isdigit():
            count = count * 10 + int(compressed[i])
            i += 1
        if i >= n:
            break
        char = compressed[i]
        i += 1
        if count == 0:
            count = 1
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "12a3b2c"
    decoded_output = decode_rle(sample_input)
    print(decoded_output)
    another_input = "4z1y0x5m"
    print(decode_rle(another_input))