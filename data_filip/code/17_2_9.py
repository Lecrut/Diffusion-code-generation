from itertools import groupby

def compress_rle(s):
    if not s:
        return ""
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        if count > 1:
            result.append(f"{char}{count}")
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    sample_strings = [
        "AAABBBCCD",
        "ABCDE",
        "AAAAA",
        "",
        "AABBCCDDEE",
        "HelloWorld"
    ]
    for s in sample_strings:
        print(compress_rle(s))