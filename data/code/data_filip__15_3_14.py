def compress(s):
    return ''.join(str(len(g)) + k for k, g in __import__('itertools').groupby(s)) if s else ''

if __name__ == '__main__':
    print(compress('bbbaaa'))