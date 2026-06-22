from itertools import groupby

def compress_rle(s):
    if not s:
        return ''
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        if count == 1:
            result.append(char)
        else:
            result.append(f"{char}{count}")
    return ''.join(result)

if __name__ == '__main__':
    samples = [
        "aabcccccaaa",
        "abcdef",
        "aaaabbbccd",
        "",
        "a"
    ]
    for sample in samples:
        print(compress_rle(sample))