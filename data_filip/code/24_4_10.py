import itertools

def rle_compress(s):
    if not s:
        return ''
    compressed = []
    for char, group in itertools.groupby(s):
        count = sum((1 for _ in group))
        compressed.append(f'{char}{count}')
    return ''.join(compressed)
if __name__ == '__main__':
    sample_string = 'aaaabbbcccdde'
    compressed_result = rle_compress(sample_string)
    print(compressed_result)