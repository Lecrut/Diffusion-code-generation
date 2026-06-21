def rle_decode(compressed):
    if not compressed:
        return ''
    result = []
    i = 0
    n = len(compressed)
    while i < n:
        count_str = ''
        while i < n and compressed[i].isdigit():
            count_str += compressed[i]
            i += 1
        if not count_str:
            count = 1
        else:
            count = int(count_str)
        if i < n:
            char = compressed[i]
            result.append(char * count)
            i += 1
    return ''.join(result)

if __name__ == '__main__':
    sample_inputs = [
        '10a',
        '2h4e3l1o',
        '1b2c3d',
        '',
        '5z',
        '100x2y'
    ]
    for s in sample_inputs:
        print(rle_decode(s))