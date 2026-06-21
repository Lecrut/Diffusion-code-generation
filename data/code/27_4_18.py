from functools import reduce

def rle_encode(s):
    return reduce(lambda acc, c: (acc[:-1] + [str(acc[-1][1] + 1) + c]) if acc and acc[-1][0] == c else (acc + [[c, 1]]) if acc else [[c, 1]], s, [])

def rle_decode(encoded):
    return reduce(lambda acc, x: acc + x[0] * int(x[1]), encoded, '')

if __name__ == '__main__':
    s = 'XYZXYZ'
    encoded = rle_encode(s)
    decoded = rle_decode(encoded)
    print(encoded)
    print(decoded)