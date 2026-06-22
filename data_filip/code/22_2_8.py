def decompress_rle(rle_string):
    if not rle_string:
        return ""
    result = []
    i = 0
    while i < len(rle_string):
        count_str = []
        while i < len(rle_string) and rle_string[i].isdigit():
            count_str.append(rle_string[i])
            i += 1
        char = rle_string[i] if i < len(rle_string) else ""
        if char:
            i += 1
        count = int("".join(count_str)) if count_str else 1
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    print(decompress_rle("2a3b"))
    print(decompress_rle("10c"))
    print(decompress_rle("1a2b3c4d"))
    print(decompress_rle(""))
    print(decompress_rle("5x"))