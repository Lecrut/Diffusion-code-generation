from itertools import groupby

def compress_string(s):
    if not s:
        return ""
    return "".join(f"{len(list(group))}{char}" for char, group in groupby(s))

if __name__ == '__main__':
    print(compress_string("aaabbbccca"))
    print(compress_string("a"))
    print(compress_string("aaabbbaaa"))