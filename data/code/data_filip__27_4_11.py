from functools import reduce

def rle_encode(s):
    return reduce(lambda acc, c: acc[:-1] + (acc[-1][0], acc[-1][1] + 1) if acc and acc[-1][0] == c else acc + [(c, 1)], s[1:], [(s[0], 1)]) if s else []

if __name__ == '__main__':
    sample = 'XYZXYZ'
    print(rle_encode(sample))