from functools import reduce
def rle_encode(s): return reduce(lambda acc, c: (acc[:-1] + (acc[-1][0], acc[-1][1] + 1) if acc and acc[-1][0] == c else acc + [(c, 1)], s) if acc else [(c, 1)], s[1:], ([], s)[1:] if len(s) > 0 else [])[0]
if __name__ == '__main__':
    sample = 'XYZXYZ'
    result = rle_encode(sample)
    print([(k, v) for k, v in result])