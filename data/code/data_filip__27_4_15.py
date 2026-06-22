from functools import reduce

def rle_encode(s):
    if not s:
        return []
    return reduce(lambda acc, c: (acc[:-1] + [(acc[-1][0], acc[-1][1] + 1)]) if acc and acc[-1][0] == c else acc + [(c, 1)], s, [])

if __name__ == '__main__':
    print(rle_encode('XYZXYZ'))