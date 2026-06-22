from itertools import groupby

def compress_rle(s):
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        result.append(f"{char}{count}")
    return "".join(result)

if __name__ == '__main__':
    print(compress_rle("aaabbc"))
    print(compress_rle("abc"))
    print(compress_rle("aaaa"))
    print(compress_rle("aabbbcccc"))