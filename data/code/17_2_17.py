import itertools

def compress_rle(s):
    if not s:
        return ''
    result = []
    for char, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        result.append(f"{char}{count}")
    return ''.join(result)

if __name__ == '__main__':
    print(compress_rle('aaabbc'))
    print(compress_rle('abba'))
    print(compress_rle(''))
    print(compress_rle('zzzzz'))