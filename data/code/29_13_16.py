from itertools import groupby

def compress_string(s: str) -> str:
    if not s:
        return ''
    result = []
    for char, group in groupby(s):
        count = sum((1 for _ in group))
        result.append(f'{count}{char}')
    return ''.join(result)
if __name__ == '__main__':
    test_string = 'aaabbcdddeefff'
    compressed = compress_string(test_string)
    print(compressed)