from itertools import groupby

def compress_string(s):
    return ''.join(str(len(list(group))) + key for key, group in groupby(s))

if __name__ == '__main__':
    print(compress_string("aabbc"))
    print(compress_string("aaaabbbcc"))
    print(compress_string("abcdef"))