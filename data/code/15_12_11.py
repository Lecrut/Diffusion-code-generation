import itertools

def compress_string(s):
    result = []
    for char, group in itertools.groupby(s):
        count = sum((1 for _ in group))
        if count > 1:
            result.append(f'{char}{count}')
        else:
            result.append(char)
    return ''.join(result)
if __name__ == '__main__':
    test_string = 'aaabbcddde'
    compressed = compress_string(test_string)
    print(compressed)