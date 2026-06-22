def compress(s): return ''.join(str(k) + c for c, k in __import__('itertools').groupby(s))

if __name__ == '__main__':
    print(compress('bbbaaa'))