def compress(s):
    return ''.join(f'{c}{sum(1 for _ in group)}' for c, group in __import__('itertools').groupby(s))

if __name__ == '__main__':
    print(compress('bbbaaa'))