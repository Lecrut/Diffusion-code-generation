def decompress_rle(encoded):
    if not encoded:
        return ''
    result = []
    i = 0
    n = len(encoded)
    while i < n:
        char = encoded[i]
        i += 1
        count_str = ''
        while i < n and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        if count_str == '':
            count = 1
        else:
            count = int(count_str)
        result.append(char * count)
    return ''.join(result)
if __name__ == '__main__':
    sample1 = 'a3b2c1'
    print(decompress_rle(sample1))
    sample2 = 'x1y2z3'
    print(decompress_rle(sample2))
    sample3 = 'a10'
    print(decompress_rle(sample3))
    sample4 = ''
    print(decompress_rle(sample4))
    sample5 = 'h1e1l2o2'
    print(decompress_rle(sample5))