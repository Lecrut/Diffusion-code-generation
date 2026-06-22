import itertools

def compress_rle(s: str) -> str:
    if not s:
        return ''
    compressed = []
    for char, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        compressed.append(f'{count}{char}')
    return ''.join(compressed)

if __name__ == '__main__':
    sample_string = 'AAAABBBCCDAA'
    result = compress_rle(sample_string)
    print(result)