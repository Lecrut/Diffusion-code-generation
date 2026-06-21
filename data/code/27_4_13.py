from functools import reduce
import itertools

def rle_encode(s):
    return reduce(lambda acc, g: acc + [(g[0], len(list(g[1])))], itertools.groupby(s), [])

if __name__ == '__main__':
    sample = 'XYZXYZ'
    print(rle_encode(sample))