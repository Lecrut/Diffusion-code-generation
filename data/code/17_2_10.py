import itertools

def compress_rle(s):
    if not s:
        return ""
    result = []
    for char, group in itertools.groupby(s):
        count = len(list(group))
        if count == 1:
            result.append(char)
        else:
            result.append(f"{char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample1 = "aaabbc"
    sample2 = "aabcccccaaa"
    sample3 = "abc"
    sample4 = ""
    print(compress_rle(sample1))
    print(compress_rle(sample2))
    print(compress_rle(sample3))
    print(compress_rle(sample4))