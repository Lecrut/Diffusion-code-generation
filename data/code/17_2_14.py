from itertools import groupby

def compress_rle(s):
    if not s:
        return ''
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        if count > 1:
            result.append(f"{count}{char}")
        else:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    print(compress_rle("aabcccccaaa"))
    print(compress_rle("abc"))
    print(compress_rle("aaabbaacc"))
    print(compress_rle(""))
    print(compress_rle("a"))