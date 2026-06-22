from functools import reduce
from itertools import groupby

def rle_encode(s):
    return reduce(lambda acc, g: acc + [(g[0], len(list(g[1])))], groupby(s), [])

if __name__ == '__main__':
    sample = 'XYZXYZ'
    print(rle_encode(sample))