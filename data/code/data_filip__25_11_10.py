def decompress_rle(encoded):
    if not encoded:
        return ""
    result = []
    i = 0
    n = len(encoded)
    while i < n:
        count_str = ""
        while i < n and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        if not count_str:
            count = 1
        else:
            count = int(count_str)
        if i < n:
            char = encoded[i]
            result.append(char * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample1 = "2a3b1c"
    print(decompress_rle(sample1))
    sample2 = "12w3z"
    print(decompress_rle(sample2))
    sample3 = ""
    print(decompress_rle(sample3))
    sample4 = "1x"
    print(decompress_rle(sample4))
    sample5 = "10a"
    print(decompress_rle(sample5))