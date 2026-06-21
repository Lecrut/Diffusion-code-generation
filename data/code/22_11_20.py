def decompress_rle(encoded_str):
    result = []
    i = 0
    n = len(encoded_str)
    while i < n:
        char = encoded_str[i]
        i += 1
        count_str = []
        while i < n and encoded_str[i].isdigit():
            count_str.append(encoded_str[i])
            i += 1
        if count_str:
            count = int("".join(count_str))
            result.append(char * count)
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "a3b2c4"
    output = decompress_rle(sample_input)
    print(output)