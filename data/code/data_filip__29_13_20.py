from itertools import groupby

def compress_string(s):
    return ''.join(f"{sum(1 for _ in g)}{k}" for k, g in groupby(s))

if __name__ == '__main__':
    print(compress_string("aaabbc"))
    print(compress_string("abc"))
    print(compress_string(""))
    print(compress_string("a"))