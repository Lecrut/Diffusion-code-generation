from functools import reduce
def rle(s): return reduce(lambda acc, c: acc + [(c, 1)] if not acc or acc[-1][0] != c else acc[:-1] + [(acc[-1][0], acc[-1][1] + 1)], s, [])
if __name__ == '__main__':
    result = rle('XYZXYZ')
    print(result)