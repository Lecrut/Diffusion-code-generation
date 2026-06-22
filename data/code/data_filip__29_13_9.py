from itertools import groupby

def compress_consecutive_duplicates(s):
    return ''.join(f"{len(list(group))}{char}" for char, group in groupby(s))

if __name__ == '__main__':
    print(compress_consecutive_duplicates('aaabbc'))
    print(compress_consecutive_duplicates('aabbbccca'))
    print(compress_consecutive_duplicates(''))
    print(compress_consecutive_duplicates('abc'))
    print(compress_consecutive_duplicates('aaaa'))