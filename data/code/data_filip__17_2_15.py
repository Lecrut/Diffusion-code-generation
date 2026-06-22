import itertools

def compress_rle(s: str) -> str:
    if not s:
        return ''
    result = []
    for char, group in itertools.groupby(s):
        count = len(list(group))
        result.append(f"{count}{char}")
    return ''.join(result)

if __name__ == '__main__':
    sample_text = "aabcccccaaa"
    compressed = compress_rle(sample_text)
    print(compressed)