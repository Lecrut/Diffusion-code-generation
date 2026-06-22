def decompress_rle(encoded_string):
    if not encoded_string:
        return ''
    result = []
    i = 0
    n = len(encoded_string)
    while i < n:
        char = encoded_string[i]
        i += 1
        count_str = ''
        while i < n and encoded_string[i].isdigit():
            count_str += encoded_string[i]
            i += 1
        count = int(count_str) if count_str else 1
        result.append(char * count)
    return ''.join(result)
if __name__ == '__main__':
    test_cases = ['a2b3c1', 'h1e1l1l1o1w1o1r1l1d2', 'a10', '', 'z1', 'ab1c2', '1a2b']
    for test in test_cases:
        result = decompress_rle(test)
        print(result)