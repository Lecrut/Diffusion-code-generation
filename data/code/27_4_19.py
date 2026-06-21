from functools import reduce
from itertools import groupby
def rle_encode(s): return ''.join(f'{k}{len(list(g))}' for k, g in groupby(s)) if s else ''
if __name__ == '__main__':
    data = 'XYZXYZ'
    print(rle_encode(data))