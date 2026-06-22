from itertools import groupby

def compress_rle(s):
    if not s:
        return ""
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        if count > 1:
            result.append(char + str(count))
        else:
            result.append(char)
    return "".join(result)

if __name__ == "__main__":
    sample1 = "aaabbbcc"
    sample2 = "abc"
    sample3 = ""
    sample4 = "a"
    sample5 = "aabcccccaaa"
    print(compress_rle(sample1))
    print(compress_rle(sample2))
    print(compress_rle(sample3))
    print(compress_rle(sample4))
    print(compress_rle(sample5))