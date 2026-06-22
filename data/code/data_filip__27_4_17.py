from functools import reduce
from itertools import groupby

def rle_encode(s):
    return reduce(lambda acc, kv: acc + (str(kv[1]) if kv[1] > 1 else '') + kv[0] if acc else kv[0], groupby(s))

if __name__ == '__main__':
    print(rle_encode('XYZXYZ'))