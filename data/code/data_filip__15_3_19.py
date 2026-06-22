def compress(s):
    return ''.join(f"{k}{len(list(g))}" for k, g in __import__('itertools').groupby(s))

if __name__ == '__main__':
    print(compress('bbbaaa'))