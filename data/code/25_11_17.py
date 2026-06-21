def decompress_rle(encoded):
    if not encoded:
        return ""
    result = []
    i = 0
    while i < len(encoded):
        count_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        if not count_str:
            count = 1
        else:
            count = int(count_str)
        if i < len(encoded):
            char = encoded[i]
            i += 1
            result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    print(decompress_rle("3A2B5C"))
    print(decompress_rle("12W"))
    print(decompress_rle("A3B"))
    print(decompress_rle(""))