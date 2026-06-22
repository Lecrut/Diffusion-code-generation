def compress(s):
    if not s:
        return ''
    return ''.join(str(len(list(g))) + k for k, g in __import__('itertools').groupby(s))

if __name__ == '__main__':
    print(compress('bbbaaa'))