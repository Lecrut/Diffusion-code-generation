from itertools import groupby

def compress_string(s):
    if not s:
        return ""
    result = []
    for key, group in groupby(s):
        count = sum(1 for _ in group)
        if count > 1:
            result.append(f"{count}{key}")
        else:
            result.append(key)
    return "".join(result)

if __name__ == '__main__':
    print(compress_string("aaabbc"))
    print(compress_string("ab"))
    print(compress_string("aabbcc"))
    print(compress_string(""))