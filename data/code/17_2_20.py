import itertools

def compress_rle(s):
    if not s:
        return ""
    result = []
    for char, group in itertools.groupby(s):
        count = len(list(group))
        result.append(f"{count}{char}")
    return "".join(result)

if __name__ == '__main__':
    sample_strings = [
        "aabcccccaaa",
        "abcdef",
        "aaaaa",
        "",
        "aabbcc"
    ]
    for s in sample_strings:
        print(compress_rle(s))