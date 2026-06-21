from itertools import groupby

def compress_run_length(s):
    return ''.join(f"{len(list(group))}{char}" for char, group in groupby(s))

if __name__ == '__main__':
    print(compress_run_length("aaaabbbcc"))
    print(compress_run_length("abcd"))
    print(compress_run_length("aabbccdd"))
    print(compress_run_length(""))
    print(compress_run_length("aaaaa"))