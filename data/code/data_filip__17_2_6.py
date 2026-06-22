from itertools import groupby

def compress_rle(s):
    if not s:
        return ""
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        result.append(f"{char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_strings = [
        "aaabbbcc",
        "abcdef",
        "aaaaa",
        "aabbbcccc",
        "",
        "a"
    ]
    for s in sample_strings:
        print(compress_rle(s))