import itertools

def compress_rle(s):
    if not s:
        return ''
    result = []
    for char, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        result.append(char)
        if count > 1:
            result.append(str(count))
    return ''.join(result)

if __name__ == '__main__':
    samples = [
        'aaabbc',
        'abcdef',
        'aaaaaa',
        '',
        'a',
        'aabbbccccd'
    ]
    for sample in samples:
        print(compress_rle(sample))